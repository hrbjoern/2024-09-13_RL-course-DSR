# 0 - Choose an alogrithm from ray.rllib.algorithms, e.g. ray.rllib.algorithms.xxx as
# xxx
# 1 - Import ray and initialize it with ray.init()
# 2 - Configure the xxx algorithm
# 2.1 - Get the default config of xxx from xxx.DEFAULT_CONFIG.copy()
# 2.2 - Examine the config and modify it if needed, e.g. change the "num_gpus" to 0,
# and the learning_rate to 0.001
import time
import gym
import ray
from ray.rllib.algorithms.dqn import dqn
ray.init()

config = dqn.DEFAULT_CONFIG.copy()
# 3 - Create an agent
# 3.1 - Creating the agent wth config and env; xxx.XXX(config=config, env="CartPole-v1")
agent = dqn.DQN(config=config, env="CartPole-v1")

# 4 - Train the agent, and examine the training reports: report = agent.train()

reports = agent.train()
print(reports)

# 5 - Run a loop for nr_trainings = 50 times agent.train()
nr_trainings = 0
for _ in range(nr_trainings):
    reports = agent.train()
    print(_, reports["episode_reward_mean"])

# 6 - Visualize the trained agent; This is similar to running the random_agent,
# except that this time we have a trained agent
# 6.1 - Create the an environment similar to the training env.
env = gym.make("CartPole-v1")
s = env.reset()
done = False
cumulative_reward = 0
while not done:
    # 6.2. Let the agent choose an action;
    a = agent.compute_single_action(observation=s, explore=False)
    # 6.3. and pass it to the environment
    s, r, done, info = env.step(action=a)
    # 6.4. How much reward did you get for that action? Keep the score!
    cumulative_reward += r
    # 6.5. Repeat the 6.{2,3, 4} until the end of the episode
# 6.6. How much total reward you got? What does it mean to have large/small reward?
print("Total reward:", cumulative_reward)

print("Good-bye.")