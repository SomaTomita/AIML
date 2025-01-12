# Assumptions of Linear Regression


############# Linearity #############
# The independent variables must have a linear relationship with the dependent variable.
# Example:
#   ** Coffee consumption and focus:
#    - A small amount of coffee improves focus. However, excessive consumption can lead to caffeine overload, reducing focus.
#   ** Exercise and weight loss:
#    - Initially, increasing exercise leads to significant weight loss.
#      However, after a certain point, weight loss plateaus, and further reduction becomes difficult.


############# No Endogeneity #############
# Endogeneity occurs when there is a correlation between the independent variables and the error term (residuals).

# Example: Relationship between rent and housing demand
# ** Exogenous variable (no endogeneity):
#   - Scenario:
#     Investigating the effect of rent on housing demand (the number of people looking to rent a house).
#   - Condition:
#     Rent (independent variable) affects demand (dependent variable) but is independent of factors included in the error term
#     (e.g., seasonal trends, population movements).
#   - Reason:
#     Rent can be evaluated as a one-way effect on demand, making it an exogenous variable (independent of the error term).

# ** Endogenous variable (with endogeneity):
#   - Scenario:
#     Higher rent reduces housing demand (rent affects demand), but higher housing demand also increases rent (demand affects rent).
#   - Situation:
#     A mutual causal relationship exists between housing demand and rent, making rent an endogenous variable
#     (independent variable correlated with the error term).
#   - Problem:
#     If the error term includes other factors influencing demand (e.g., economic trends, interest rates),
#     rent and the error term become correlated, making the model unreliable.


############# Normality and Homoscedasticity #############
# Residuals must follow a normal distribution.
# In other words, residuals should result from random prediction errors, with most values close to the mean and fewer extreme outliers.


############# No Autocorrelation #############
# Residuals must not exhibit autocorrelation (residuals should be randomly distributed,
# and one residual should not influence another).

# Example:
# ** No autocorrelation:
#   - Predicting test scores based on study time: Each student's study time and scores are independent of other students'.
#     One student's test results do not influence another's.
#   - Predicting sales based on advertising expenses: Daily sales are assumed to be independent.
#     For instance, today's advertising impact does not influence yesterday's sales.

# ** Autocorrelation exists:
#   - Predicting daily sales: Yesterday's sales may influence today's sales.
#   - Predicting daily weather: Yesterday's weather may affect today's weather.


############# No Multicollinearity #############
# The independent variables must not exhibit strong correlation with each other.
# In other words, having multiple variables with similar information can destabilize the regression model's estimates.
