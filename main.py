import numpy as np
import gymnasium as gym

from pid import PID
from cartpole_continuous import CartPoleContinuousEnv

gym.register(id='CartPoleContinuous', entry_point='cartpole_continuous:CartPoleContinuousEnv')

env = gym.make('CartPoleContinuous', render_mode='human')
obs, _ = env.reset()

angle_pid = PID(0.5, 0., 1.2, None, (-1., 1))
angle_rate_pid = PID(1., 0., 0.)

while True:
    action = angle_rate_pid.update(angle_pid.update(obs[2], 0.), 0.)
    # action = env.action_space.sample()
    obs, reward, done, _, info = env.step(np.array([action]).astype(np.float32))

    env.render()

    if done:
        break

env.close()
