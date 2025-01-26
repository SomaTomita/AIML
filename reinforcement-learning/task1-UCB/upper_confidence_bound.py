############# Upper Confidence Bound (UCB) #############

import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("reinforcement-learning/task1-UCB/Ads_CTR_Optimisation.csv")

import math

N = 10000
d = 10
ads_selected = []
# The reward is a value in the data set (0 or 1), where 1 means “ad clicked”. If the selection history for ad 1 is [1, 0, 1, 0], the cumulative reward is 1+0+1+0=2.
numbers_of_selections = [0] * d  # [0, 0, ... ]
sums_of_rewards = [0] * d
total_reward = 0
for n in range(0, N):
    ad = 0
    max_upper_bound = 0
    for i in range(0, d):
        if numbers_of_selections[i] > 0:
            # If ad 1 was selected 5 times and clicked on 3 of those times: sums_of_rewards=3
            #  sums_of_rewards=3 (number of clicks)
            #  numbers_of_selections=5 (number of selections)
            average_reward = sums_of_rewards[i] / numbers_of_selections[i]
            #  Denominator and numerator of the confidence interval: log
            #  (n+1): serves to reduce exploration as the number of attempts increases.
            # numbers_of_selections[i]: Well-selected ads reduce exploration and increase utilization.
            delta_i = math.sqrt(3 / 2 * math.log(n + 1) / numbers_of_selections[i])

            upper_bound = average_reward + delta_i
        else:
            # ads with no attempts have infinite UCB values
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            # The sum of the mean reward and the confidence interval selects the advertisement with the highest value.
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    numbers_of_selections[ad] = numbers_of_selections[ad] + 1
    reward = dataset.values[n, ad]
    sums_of_rewards[ad] = sums_of_rewards[ad] + reward
    total_reward = total_reward + reward

# Visualising the results
plt.hist(ads_selected)
plt.title("Histogram of ads selections")
plt.xlabel("Ads")
plt.ylabel("Number of times each ad was selected")
plt.show()
