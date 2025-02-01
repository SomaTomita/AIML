############# Question #############

# Suppose you have a convolutional neural network with an 9x9x3 input volume representing a colour image.
# The first layer is a convolutional layer consisting of 10 filters that have a 4x4x3 receptive field.
# Calculate the number of neurons and the total number of weights in the first layer.

# Neurons:
# Weights:

# The output of the first layer is a volume. Give its dimensions.
# Output volume dimensions:


############# Answer #############
# eurons: 360
# Weights: 480
# Output Volume Dimensions: 6*6*10


# ------------------------------------------------------------------------------
# Detailed Explanation (commented)
# ------------------------------------------------------------------------------
# 1. Calculate Output Volume Dimensions:
#    Formula: O = (I - F) / S + 1
#    - Input size (I) = 9
#    - Filter size (F) = 4
#    - Stride (S) = 1
#    - No padding (valid convolution)
#    Calculation: (9 - 4) / 1 + 1 = 6
#    Output volume dimensions = 6 x 6 x 10

# 2. Calculate Number of Neurons:
#    - Each neuron corresponds to one position in the output volume.
#    - Total neurons = 6 x 6 x 10 = 360

# 3. Calculate Number of Weights:
#    - Each filter has weights for a 4 x 4 x 3 region.
#    - Weights per filter = 4 x 4 x 3 = 48
#    - There are 10 filters.
#    - Total weights = 48 x 10 = 480
# ------------------------------------------------------------------------------
