import array
from typing import List
from xmlrpc.client import Boolean
from gymnasium import spaces
import gymnasium as gym
import numpy as np


class MyGymPointsEnv(gym.Env):
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 4}
    max_size = 10
    epsilon = 0.01

    def __init__(self, a: int = 10, b: int = 10, max_size=10):
        self.max_size = max_size
        self.size = (a, b)
        self.points: np.ndarray = np.zeros((self.max_size, 4), dtype=np.float32)
        self.low = np.tile(np.array([0, 0, -max(a, b), -np.pi]), (self.max_size, 1))
        self.high = np.tile(np.array([a, b, max(a, b), np.pi]), (self.max_size, 1))
        self.observation_space = spaces.Box(self.low, self.high, (self.max_size, 4))
        self.action_space = spaces.Box(-1.0, 1.0, shape=(3,), dtype=np.float32)
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
        # observation, reward, terminated, False, info
        action = np.clip(action, -1.0, 1.0, dtype=np.float32)
        target = int(np.abs(action[0] - (-1.0), dtype=np.float32) * self.max_size / 2)
        delta_angle = action[1] * np.pi
        delta_velocity = action[2] * max(self.size)
        changed_angle = np.clip(self.points[target][3] + delta_angle, -np.pi, np.pi)
        changed_velocity = np.clip(
            self.points[target][2] + delta_velocity, -max(self.size), max(self.size)
        )
        self.points[target][3] = changed_angle
        self.points[target][2] = changed_velocity
        state = [
            self.points[:, 0],
            self.points[:, 1],
            self.points[:, 2],
            self.points[:, 3],
        ]
        reward = 0.0
        terminated = False
        if not (changed_angle == 0.0 and changed_velocity == 0.0):
            reward -= 1.0
        if not (self._check_collisions()):
            reward += 3.0
        else:
            terminated = True
            reward -= 5.0
        return np.array(state, dtype=np.float32), reward, terminated, False, {}

    def _check_collisions(self) -> Boolean:
        """
        Check for collisions between points and return a boolean indicating if any collisions were found.
        Return: True if any collisions were found, False otherwise.
        """
        for i in range(len(self.points)):
            for j in range(i + 1, len(self.points)):
                distance = (
                    (self.points[i][0] - self.points[j][0]) ** 2
                    + (self.points[i][1] - self.points[j][1]) ** 2
                ) ** 0.5
                if distance < self.epsilon:
                    # handle collision
                    return True
        return False

    def _get_obs(self):
        return [
            self.points[:, 0],
            self.points[:, 1],
            self.points[:, 2],
            self.points[:, 3],
        ]

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.points = np.zeros(self.points.shape, dtype=np.float32)
        observation = self._get_obs()

        return np.array(observation, dtype=np.float32), {}
