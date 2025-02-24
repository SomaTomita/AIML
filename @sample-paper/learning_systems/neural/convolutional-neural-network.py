############# Question #############

# Suppose you have a convolutional neural network with an 9x9x3 input volume representing a colour image.
# The first layer is a convolutional layer consisting of 10 filters that have a 4x4x3 receptive field.
# Calculate the number of neurons and the total number of weights in the first layer.

# Neurons:
# Weights:

# The output of the first layer is a volume. Give its dimensions.
# Output volume dimensions:


############# Answer #############
# Neurons: 360
# Weights: 490 (include the bias term (48 + 1 = 49 per filter))
# Output Volume Dimensions: 6 × 6 × 10

# ------------------------------------------------------------------------------
# Detailed Explanation
# ------------------------------------------------------------------------------
# 1. Calculate Output Volume Dimensions:
#    Formula: O = (I - F) / S + 1
#    - Input size (I)  = 9
#    - Filter size (F) = 4
#    - Stride (S)      = 1
#    - No padding (valid convolution)
#    Calculation: (9 - 4) / 1 + 1 = 6
#    => Output volume dimensions = 6 × 6 × 10

# 2. Calculate Number of Neurons:
#    - Each neuron corresponds to one output element in the 6 × 6 × 10 volume
#    - Total neurons = 6 × 6 × 10 = 360

# 3. Calculate Number of Weights:
#    - Each filter spans a 4 × 4 × 3 region = 48 weights per filter
#    - Include 1 bias weight per filter → 48 + 1 = 49
#    - There are 10 filters
#    => Total weights = 49 × 10 = 490
# ------------------------------------------------------------------------------


# Input Grid Representation (9x9):
#    - This grid represents a 9x9 input image, where each cell corresponds to a pixel.
#    - The values in the cells represent the (row, column) coordinates.
#
#    Example:
#      0,0  0,1  0,2  0,3  0,4  0,5  0,6  0,7  0,8
#      1,0  1,1  1,2  1,3  1,4  1,5  1,6  1,7  1,8
#      ...
#      8,0  8,1  8,2  8,3  8,4  8,5  8,6  8,7  8,8

# The filter starts at (0,0) and moves one column to the right because the stride is 1.
# The first application position is (0,0), where the filter covers (0,0) through (3,3).
# Next, it moves one column to the right, covering (0,1) through (3,4).
# This continues until the filter reaches the last column (5,5).
# The last covered area is (0,5) through (3,8) in the input grid as the filter moves one step (stride = 1) to the right.

# ------------------------------------------------------------------------------
# Filter Application Grid (4x4 filter with stride 1)
#    - 'F' marks where the top-left corner of a filter can be placed.
#    - Each filter spans a 4x4 region, covering a total of 16 input pixels at a time.
#    - The filter moves one step (stride = 1) to the right until it reaches the last possible position.
#    - The filter cannot be placed beyond the 5th column (0-based index) because it would exceed the input grid's boundaries.
#
#    Example (Filter Placement):
#      F   F   F   F   F   F
#      F   F   F   F   F   F
#      F   F   F   F   F   F
#      F   F   F   F   F   F
#      F   F   F   F   F   F


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
############# Question 1 #############

# Suppose you have a convolutional neural network with a 12×12×3 input volume representing a color image.
# The first layer is a convolutional layer consisting of 8 filters that have a 5×5×3 receptive field.

### Tasks:
# 1. Calculate the number of neurons in the first layer.
# 2. Calculate the total number of weights in the first layer.
# 3. Give the dimensions of the output volume.

### Assumptions:
# - Stride: 1
# - No padding (valid convolution)

# Neurons:
# Weights:
# Output volume dimensions:

############# Answer1 #############
# Neurons: 512
# Weights: 608
# Output volume dimensions: 8 * 8 * 8

# ------------------------------------------------------------------------------
# Explanation for Question 1
# ------------------------------------------------------------------------------
# 1. Calculate Output Volume Dimensions:
#    Formula: O = (I - F) / S + 1
#    - Input size (I)  = 12
#    - Filter size (F) = 5
#    - Stride (S)      = 1
#    - No padding (valid convolution)
#    Calculation: (12 - 5) / 1 + 1 = 8
#    => Output volume dimensions = 8 × 8 × 8 (width × height × #filters)

# 2. Calculate Number of Neurons:
#    - Each neuron corresponds to one position in the 8 × 8 × 8 output volume.
#    - Total neurons = 8 × 8 × 8 = 512

# 3. Calculate Number of Weights:
#    - Each filter spans a 5 × 5 × 3 region = 75 weights per filter.
#    - Include 1 bias weight per filter → 75 + 1 = 76.
#    - There are 8 filters.
#    => Total weights = 76 × 8 = 608
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
############# Question 2 #############
# You are designing a convolutional neural network that takes a 16×16×3 input volume.
# The first layer is a convolutional layer with 6 filters, each with a 3×3×3 receptive field.

### Tasks:
# 1. Calculate the number of neurons in the first layer.
# 2. Calculate the total number of weights in the first layer.
# 3. Give the dimensions of the output volume.

### Assumptions:
# - Stride: 2
# - Padding: "same" (zero-padding so that output size remains divided cleanly by stride)

# Neurons:
# Weights:
# Output volume dimensions:

############# Answer 2 #############
# Neurons: 64 × 6 = 384
# Weights: 3 × 3 × 3 + 1 = 28 per filter → 28 × 6 = 168
# Output Volume Dimensions: 8 × 8 × 6

# ------------------------------------------------------------------------------
# Explanation for Question 2
# ------------------------------------------------------------------------------
# 1. Calculate Output Volume Dimensions:
#    Formula for "same" padding:
#    O = ⌈ I / S ⌉   (since padding ensures output remains integer)
#    - Input size (I)  = 16
#    - Filter size (F) = 3
#    - Stride (S)      = 2
#    - Padding type    = "same" (automatically adjusts input with zero-padding)
#    Calculation: ⌈ 16 / 2 ⌉ = 8
#    => Output volume dimensions = 8 × 8 × 6

# ------------------------------------------------------------------------------
# Visual Explanation of Stride 2 with "same" padding
# ------------------------------------------------------------------------------
# Input Grid (16x16):
#    0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
#    1  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#    2  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#    ...
#
# Filter Movement with Stride 2:
# F = Filter starting position (3x3)
# Numbers show the output position that each filter application produces
#
#    F→F→F→F→F→F→F→F
#    1 2 3 4 5 6 7 8    Each row produces 8 outputs because:
#    ↓                  - Start at position 0
#    F→F→F→F→F→F→F→F    - Move 2 steps each time (stride=2)
#    1 2 3 4 5 6 7 8    - Cover all 16 positions with 8 steps
#    ...
# → Since the stride is 2, the output size is half of the input size.
#    (16 → 8, because we move 2 pixels per step)
#
# Why O = I/S works:
# - With 16 input positions and stride 2:
# - First filter position: covers positions 0,1,2
# - Second filter position: covers positions 2,3,4 (starting at position 2)
# - Third filter position: covers positions 4,5,6
# - And so on...
# - This creates 16/2 = 8 output positions in each dimension
#
# "same" padding ensures:
# - The filter can be centered on the first and last input positions
# - Output size is always input_size/stride (rounded up if needed)
# - Padding is added automatically to maintain this relationship

# 2. Calculate Number of Neurons:
#    - Each neuron corresponds to one position in the 8 × 8 × 6 output volume.
#    - Total neurons = 8 × 8 × 6 = 384

# 3. Calculate Number of Weights:
#    - Each filter spans a 3 × 3 × 3 region = 27 weights per filter.
#    - Include 1 bias weight per filter → 27 + 1 = 28.
#    - There are 6 filters.
#    => Total weights = 28 × 6 = 168
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
############# Question 3 #############
# You have a convolutional neural network with a 20×20×3 input volume representing a color image.
# The first layer is a convolutional layer with 12 filters, each with a 5×5×3 receptive field.

### Tasks:
# 1. Calculate the number of neurons in the first layer.
# 2. Calculate the total number of weights in the first layer.
# 3. Give the dimensions of the output volume.

### Assumptions:
# - Stride: 2
# - No padding (valid convolution)

# Neurons:
# Weights:
# Output volume dimensions:

############# Answer 3 #############
# Neurons: 864
# Weights: 912
# Output Volume Dimensions: 8 × 8 × 12

# ------------------------------------------------------------------------------
# Explanation for Question 3
# ------------------------------------------------------------------------------
# 1. Calculate Output Volume Dimensions:
#    Formula: O = (I - F) / S + 1
#    - Input size (I)  = 20
#    - Filter size (F) = 5
#    - Stride (S)      = 2
#    - No padding
#    Calculation: (20 - 5) / 2 + 1 = 8
#    => Output volume dimensions = 8 × 8 × 12

# 2. Calculate Number of Neurons:
#    - Each neuron corresponds to one position in the 8 × 8 × 12 output volume
#    - Total neurons = 8 × 8 × 12 = 864

# 3. Calculate Number of Weights:
#    - Each filter spans a 5 × 5 × 3 region = 75 weights per filter
#    - Include 1 bias weight per filter → 75 + 1 = 76
#    - There are 12 filters
#    => Total weights = 76 × 12 = 912
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
############# Question 4 #############
# Consider a convolutional neural network with a 15×15×1 input volume (grayscale image).
# The first layer is a convolutional layer with 16 filters, each with a 3×3×1 receptive field.

### Tasks:
# 1. Calculate the number of neurons in the first layer.
# 2. Calculate the total number of weights in the first layer.
# 3. Give the dimensions of the output volume.

### Assumptions:
# - Stride: 1
# - Padding: "same"

# Neurons:
# Weights:
# Output volume dimensions:

############# Answer 4 #############
# Neurons: 3600
# Weights: 160
# Output Volume Dimensions: 15 × 15 × 16

# ------------------------------------------------------------------------------
# Explanation for Question 4
# ------------------------------------------------------------------------------
# 1. Calculate Output Volume Dimensions:
#    With "same" padding:
#    - Input size remains unchanged when stride = 1
#    - Output width = input width = 15
#    - Output height = input height = 15
#    - Depth = number of filters = 16
#    => Output volume dimensions = 15 × 15 × 16

# 2. Calculate Number of Neurons:
#    - Each neuron corresponds to one position in the 15 × 15 × 16 output volume
#    - Total neurons = 15 × 15 × 16 = 3600

# 3. Calculate Number of Weights:
#    - Each filter spans a 3 × 3 × 1 region = 9 weights per filter
#    - Include 1 bias weight per filter → 9 + 1 = 10
#    - There are 16 filters
#    => Total weights = 10 × 16 = 160
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
############# Question 5 #############
# Consider a convolutional neural network with a 24×24×1 input volume (grayscale image).
# The first layer is a convolutional layer with 8 filters, each with a 4×4×1 receptive field.

### Tasks:
# 1. Calculate the number of neurons in the first layer.
# 2. Calculate the total number of weights in the first layer.
# 3. Give the dimensions of the output volume.

### Assumptions:
# - Stride: 2
# - Padding: "same"

# Neurons:
# Weights:
# Output volume dimensions:

############# Answer 5 #############
# Neurons: 768
# Weights: 136
# Output Volume Dimensions: 12 × 12 × 8

# ------------------------------------------------------------------------------
# Explanation for Question 5
# ------------------------------------------------------------------------------
# 1. Calculate Output Volume Dimensions:
#    Formula for "same" padding with stride:
#    O = ⌈ I / S ⌉
#    - Input size (I)  = 24
#    - Filter size (F) = 4
#    - Stride (S)      = 2
#    - Padding type    = "same"
#    Calculation: ⌈ 24 / 2 ⌉ = 12
#    => Output volume dimensions = 12 × 12 × 8

# 2. Calculate Number of Neurons:
#    - Each neuron corresponds to one position in the 12 × 12 × 8 output volume
#    - Total neurons = 12 × 12 × 8 = 768

# 3. Calculate Number of Weights:
#    - Each filter spans a 4 × 4 × 1 region = 16 weights per filter
#    - Include 1 bias weight per filter → 16 + 1 = 17
#    - There are 8 filters
#    => Total weights = 17 × 8 = 136
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
############# Question 6 #############
# You have a convolutional neural network with a 18×18×3 input volume representing a color image.
# The first layer is a convolutional layer with 16 filters, each with a 3×3×3 receptive field.

### Tasks:
# 1. Calculate the number of neurons in the first layer.
# 2. Calculate the total number of weights in the first layer.
# 3. Give the dimensions of the output volume.

### Assumptions:
# - Stride: 1
# - No padding (valid convolution)

# Neurons:
# Weights:
# Output volume dimensions:

############# Answer 6 #############
# Neurons: 4096
# Weights: 448
# Output Volume Dimensions: 16 × 16 × 16

# ------------------------------------------------------------------------------
# Explanation for Question 6
# ------------------------------------------------------------------------------
# 1. Calculate Output Volume Dimensions:
#    Formula: O = (I - F) / S + 1
#    - Input size (I)  = 18
#    - Filter size (F) = 3
#    - Stride (S)      = 1
#    - No padding
#    Calculation: (18 - 3) / 1 + 1 = 16
#    => Output volume dimensions = 16 × 16 × 16

# 2. Calculate Number of Neurons:
#    - Each neuron corresponds to one position in the 16 × 16 × 16 output volume
#    - Total neurons = 16 × 16 × 16 = 4096

# 3. Calculate Number of Weights:
#    - Each filter spans a 3 × 3 × 3 region = 27 weights per filter
#    - Include 1 bias weight per filter → 27 + 1 = 28
#    - There are 16 filters
#    => Total weights = 28 × 16 = 448
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
############# Question 7 #############

# Suppose you have a convolutional neural network with an 8x8x3 input volume representing a colour image.
# The first layer is a convolutional layer consisting of 10 filters that have a 3x3x3 receptive field.
# Calculate the number of neurons and the total number of weights in the first layer.

# Neurons:
# Weights:
# The output of the first layer is a volume. Give its dimensions.
# Output volume dimensions:

############# Answer 7 #############
# ------------------------------------------------------------------------------
# Explanation for Question 7
# ------------------------------------------------------------------------------
# 1. Calculate Output Volume Dimensions:
#    Formula: O = (I - F) / S + 1
#    - Input size (I)  = 8
#    - Filter size (F) = 3
#    - Stride (S)      = 1
#    - No padding (valid convolution)
#    Calculation: (8 - 3) / 1 + 1 = 6
#    => Output volume dimensions = 6 × 6 × 10

# 2. Calculate Number of Neurons:
#    - Each neuron corresponds to one output element in the 6 × 6 × 10 volume
#    - Total neurons = 6 × 6 × 10 = 360

# 3. Calculate Number of Weights:
#    - Each filter spans a 3 × 3 × 3 region = 27 weights per filter
#    - Include 1 bias weight per filter → 27 + 1 = 28
#    - There are 10 filters
#    => Total weights = 28 × 10 = 280
# ------------------------------------------------------------------------------
