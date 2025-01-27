# Thompson Sampling

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(
    "reinforcement-learning/task2-thompson_sampling/Ads_CTR_Optimisation.csv"
)


import random

N = 10000
d = 10
ads_selected = []
# alike UCB, These lists will track how many times each ad gets a positive reward (1) or a negative reward (0)
numbers_of_rewards_1 = [0] * d
numbers_of_rewards_0 = [0] * d
total_reward = 0
for n in range(0, N):
    ad = 0
    max_random = 0
    for i in range(0, d):
        # Generate a random sample from the Beta distribution for each ad
        random_beta = random.betavariate(
            numbers_of_rewards_1[i] + 1, numbers_of_rewards_0[i] + 1
        )
        if random_beta > max_random:
            max_random = random_beta
            ad = i
    ads_selected.append(ad)
    reward = dataset.values[n, ad]
    if reward == 1:
        numbers_of_rewards_1[ad] = numbers_of_rewards_1[ad] + 1
    else:
        numbers_of_rewards_0[ad] = numbers_of_rewards_0[ad] + 1
    total_reward = total_reward + reward


# Visualising the results
plt.hist(ads_selected)
plt.title("Histogram of ads selections")
plt.xlabel("Ads")
plt.ylabel("Number of times each ad was selected")
plt.show()


# the difference between UCB vs Thompson sampling
# Probabilistic Nature:
# - Thompson Sampling is inherently probabilistic and is based on sampling from a distribution (e.g., a Beta or Gaussian distribution) to decide which arm (option) to pull. The algorithm considers uncertainty in a probabilistic manner.
# - UCB (Upper Confidence Bound), on the other hand, does not rely on sampling from a distribution but instead calculates a deterministic confidence bound based on the observed rewards and the number of times an arm has been selected.
# Reflection of Feedback:
# - UCB requires immediate updates based on the observed reward. For example, in the case of advertisements, the algorithm updates its confidence bound after every click or interaction to reflect the most recent information.
# - Thompson Sampling, however, adjusts the algorithm based on observed results in a more flexible manner. It samples from posterior distributions that are updated over time using prior knowledge and new data, allowing it to incorporate uncertainty in its decision-making process.
