import random 
from tqdm import tqdm

# Here you create an env and let an agent interact with it. You can measure how
# successful is the random agent, i.e. how much reward it accumulates.

# 0 - Create an env
import gymnasium as gym
env = gym.make("CartPole-v1", render_mode="rgb_array")

# 1 - Reset the env.
env.reset()
# 2 - Let a random agent interact with the env.

#sum = 0 
sumlist = 0
numtrials = 10000

# 2.1. Choose a random action (with in the action space of the env.)

for _ in tqdm(range(numtrials)):
#for _ in range(numtrials):
    running = True 
    env.reset()
    sum = 0
    while running:
        a =  random.randint(0, 1)
        #print(a)

        # 2.2. and pass it to the environment
        #print(env.step(a))

        # 2.3. How much reward did you get for that action? Keep the score!
        sprime = env.step(a)
        reward, running = sprime[1], (not sprime[2])
        if numtrials <= 10: 
            print(_, a, reward)

        sum += reward
    sumlist += sum

print("Result: ", sumlist/numtrials)


# 2.4. Repeat the 2.{1,2,3} until the end of the episode


# 2.5. How much total reward you got? What does it mean to have large/small reward?

# 3. Repeat the whole section 2. Do you get the same total reward?