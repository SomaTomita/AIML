# Calculate the probability of actually having the disease if the test result is positive.

# Define probabilities
p_disease = 0.01  # P(Disease)
p_no_disease = 1 - p_disease  # P(No Disease)
p_positive_given_disease = 0.99  # P(Positive|Disease)
p_positive_given_no_disease = 0.05  # P(Positive|NoDisease)

# Total probability of Positive (P(Positive))
"""
When a positive test is given in the presence of actual disease
 +
When a false positive test occurs when there is no disease
"""
p_positive = (p_positive_given_disease * p_disease) + (
    p_positive_given_no_disease * p_no_disease
)

# Calculate P(Disease|Positive) using Bayes' theorem
p_disease_given_positive = (p_positive_given_disease * p_disease) / p_positive

# Display the result
print(
    f"The probability of having the disease given a positive test result is: {p_disease_given_positive:.2%}"
)
