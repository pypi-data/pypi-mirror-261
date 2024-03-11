from os import path
from PIL import Image, ImageDraw
from typing import List
from xmlrpc.client import Boolean
from gymnasium import spaces
import gymnasium as gym
import numpy as np


class MyGymPointsEnv(gym.Env):
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 4}
    max_size = 10
    epsilon = 0.01

    def __init__(
        self,
        a=10,
        b=10,
        max_size=10,
        verbose=False,
        image_path="",
    ):
        self.verbose = verbose
        self.max_size = max_size
        self.size = (a, b)
        self.step_num = 0
        self.points = self._generate_points()
        self.image_path = image_path
        while self._check_collisions():
            self.points = self._generate_points()
        # self.low = np.array([-a / 2, -b / 2, -max(a, b), -np.pi]).astype(np.float32)
        # self.high = np.array([a / 2, b / 2, max(a, b), np.pi]).astype(np.float32)
        self.observation_space = spaces.Box(-1.0, 1.0, (self.max_size, 4))
        # self.action_space = spaces.Discrete(
        #     5
        # )  # 0 -- nop, 1 -- slow down, 2 -- speed up, 3 -- rotate left, 4 -- rotate right
        self.action_space = spaces.Box(-1.0, 1.0, shape=(3,), dtype=np.float32)
        # 0 -- pos_x
        # 1 -- pos_y
        # 2 -- velocity
        # 3 -- angle(vector)
        #     np.reshape(
        #         np.repeat(np.array([0, -np.pi, -max(a, b)]), self.max_size),
        #         (self.max_size, 3),
        #     ),
        #     np.reshape(
        #         np.repeat(np.array([self.max_size, np.pi, max(a, b)]), self.max_size),
        #         (self.max_size, 3),
        #     ),
        # )

    def step(self, action):
        reward = 0.0
        if self.verbose:
            print(action)
        target = int(action[0] * (self.max_size - 1) / 2)
        change_velocity = action[1] * max(self.size)
        change_angle = action[2] * np.pi
        if self.verbose:
            print(
                f"target: {target}",
                f"change_velocity: {change_velocity}",
                f"change_angle: {change_angle}",
            )
        self.points[target][2] += change_velocity
        self.points[target][2] = np.clip(
            self.points[target][2], -max(self.size), max(self.size)
        )
        self.points[target][3] += change_angle
        self.points[target][3] = np.clip(self.points[target][3], -np.pi, np.pi)
        if np.abs(action[1]) < self.epsilon and np.abs(action[2]) < self.epsilon:
            reward += 1.0
        else:
            reward -= 1.0
        # observation, reward, terminated, False, info
        self._move_forward()
        self._draw_state_image(f"{self.step_num}")
        terminated = False
        if not (self._check_collisions()):
            reward += 3.0
        else:
            terminated = True
            reward -= 5.0

        self.step_num += 1
        return (
            self._get_obs(),
            reward,
            terminated,
            False,
            {},
        )

    def _recoil_from_bounds(self):
        # Recoil points if they are about to go out of image bounds
        margin = 1  # Margin to determine when points should recoil

        # Check x-coordinate bounds
        mask_x_lower = self.points[:, 0] < margin
        mask_x_upper = self.points[:, 0] > (self.size[0] - margin)
        self.points[mask_x_lower, 3] += np.pi
        self.points[mask_x_upper, 3] += np.pi

        # Check y-coordinate bounds
        mask_y_lower = self.points[:, 1] < margin
        mask_y_upper = self.points[:, 1] > (self.size[1] - margin)
        self.points[mask_y_lower, 3] += np.pi
        self.points[mask_y_upper, 3] -= np.pi
        self.points[:, 3] = (self.points[:, 3] + np.pi) % (2 * np.pi) - np.pi

    def _move_forward(self, dt=0.1):
        # Update the positions of points based on their velocity and angle
        # Using Euler integration scheme
        self.points[:, 3] = (self.points[:, 3] + np.pi) % (2 * np.pi) - np.pi
        self.points[:, 0] += (
            self.points[:, 2] * np.cos(self.points[:, 3]) * dt
        )  # Update x positions
        self.points[:, 1] += (
            self.points[:, 2] * np.sin(self.points[:, 3]) * dt
        )  # Update y positions

        self._recoil_from_bounds()

    def _check_collisions(self) -> Boolean:
        """
        Check for collisions between points and return a boolean indicating if any collisions were found.
        Return: True if any collisions were found, False otherwise.
        """
        for i in range(len(self.points)):
            for j in range(i + 1, len(self.points)):
                if (
                    self.points[i][0] == self.points[j][0]
                    and self.points[i][1] == self.points[j][1]
                ):
                    return True
        return False

    def _get_obs(self):
        return np.array(
            [
                self.points[:, 0] / (self.size[0]),
                self.points[:, 1] / (self.size[1]),
                self.points[:, 2] / (max(self.size)),
                self.points[:, 3] / (np.pi),
            ],
            dtype=np.float32,
        ).T

    def _generate_points(self):

        x_values = np.random.randint(0, self.size[0], size=self.max_size)
        y_values = np.random.randint(0, self.size[1], size=self.max_size)
        velocity_values = np.random.uniform(0, max(self.size), size=self.max_size)
        angle_values = np.random.uniform(-np.pi, np.pi, size=self.max_size)

        # Combine the values into self.points
        return np.column_stack((x_values, y_values, velocity_values, angle_values))

    def _draw_state_image(self, image_name: str):
        image_size = self.size  # Replace this with your desired image size
        image = Image.new(
            "L", image_size, color=0
        )  # 'L' mode represents a grayscale image

        # Create a draw object
        draw = ImageDraw.Draw(image)

        # Assuming self.points is a NumPy array with shape [10, 4]
        for point in self.points:
            x, y = (
                point[0],
                point[1],
            )  # Adjust for positive coordinates
            draw.point((x, y), fill=255)  # Set pixel to white

        # Save or display the image
        image_path = path.join(self.image_path, image_name + ".png")
        print(image_path)
        image.save(image_path)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.points = self._generate_points()
        while self._check_collisions():
            self.points = self._generate_points()
        observation = self._get_obs()

        return np.array(observation, dtype=np.float32), {}


# env = MyGymPointsEnv(
#     20, 20, 10, image_path="C:\\Users\\anton\\MachineLearning\\PointsCollision\\images"
# )
# env.reset()
# env.step([0, 0, 0])
