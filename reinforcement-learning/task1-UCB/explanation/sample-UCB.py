# debug

import math

# Imagine we have 3 ads and their reward probabilities are simulated manually
# 1 = user clicked the ad (reward), 0 = no click
ads_data = [
    [1, 0, 1, 1, 0],  # Ad 1: Simulated rewards for 5 rounds
    [0, 1, 0, 0, 1],  # Ad 2: Simulated rewards for 5 rounds
    [1, 1, 1, 0, 0],  # Ad 3: Simulated rewards for 5 rounds
]


N = 5  # Number of rounds (iterations)
d = len(ads_data)  # Number of ads
numbers_of_selections = [0] * d
sums_of_rewards = [0] * d
ads_selected = []

for n in range(0, N):
    print(f"Round {n + 1}:")  # Debugging output for each round
    max_upper_bound = 0
    selected_ad = 0

    # Calculate UCB for each ad
    for i in range(0, d):
        if numbers_of_selections[i] > 0:
            average_reward = sums_of_rewards[i] / numbers_of_selections[i]
            delta_i = math.sqrt(3 / 2 * math.log(n + 1) / numbers_of_selections[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = float("inf")

        print(
            f"  Ad {i + 1}: Average Reward = {average_reward if numbers_of_selections[i] > 0 else 'N/A'}, "
            f"Delta = {delta_i if numbers_of_selections[i] > 0 else 'N/A'}, Upper Bound = {upper_bound}"
        )

        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            selected_ad = i

    ads_selected.append(selected_ad)
    numbers_of_selections[selected_ad] += 1

    reward = ads_data[selected_ad][n]
    sums_of_rewards[selected_ad] += reward

    # Debugging output after selecting the ad
    print(f"  Selected Ad: {selected_ad + 1}")
    print(f"  Updated Numbers of Selections: {numbers_of_selections}")
    print(f"  Updated Sums of Rewards: {sums_of_rewards}\n")

# Output results
print("Final Results:")
print("Ads selected in each round:", ads_selected)
print("Number of times each ad was selected:", numbers_of_selections)
print("Cumulative rewards for each ad:", sums_of_rewards)


# Explanation:
# ads_selected - Shows which ad was selected in each round (e.g., [0, 1, 2, 0, 1])
# numbers_of_selections - Shows how many times each ad was selected (e.g., [2, 2, 1])
# sums_of_rewards - Shows the total reward collected from each ad (e.g., [3, 1, 2])
