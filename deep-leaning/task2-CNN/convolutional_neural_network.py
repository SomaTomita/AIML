# Convolutional Neural Network


from tkinter.ttk import _Padding
from warnings import filters
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator


# Part 1 - Data Preprocessing
# Generating images for the Training set
train_datagen = ImageDataGenerator(
    rescale=1.0
    / 255,  # Change pixel values from [0, 255] to [0, 1] (makes learning easier)
    shear_range=0.2,  # Slightly slants the image in one direction (adds variety)
    zoom_range=0.2,  # Randomly zooms in or out (helps the model handle different sizes)
    horizontal_flip=True,  # Randomly flips images left and right (helps with different orientations)
)
# Generating images for the Test set
test_datagen = ImageDataGenerator(rescale=1.0 / 255)
# Creating the Training set
training_set = train_datagen.flow_from_directory(
    "deep-leaning/task2-CNN/dataset/training_set",  # Folder containing training images
    target_size=(
        64,
        64,
    ),  # Resize all images to 64x64 pixels (to match model input size)
    batch_size=32,  # Number of images the model processes at one time
    class_mode="binary",  # There are only two categories (e.g., cat or dog)
)
# Creating the Test set
test_set = test_datagen.flow_from_directory(
    "deep-leaning/task2-CNN/dataset/training_set",
    target_size=(64, 64),
    batch_size=32,
    class_mode="binary",
)


# Part 2 - Building the CNN
# Initialising the CNN
cnn = tf.keras.models.Sequential()

# Step 1 - Convolution
# Add a 2D convolutional layer to the CNN
cnn.add(
    tf.keras.layers.Conv2D(
        filters=32,  # Number of filters (patterns the model learns)
        kernel_size=3,  # Size of each filter (3x3 pixels)
        padding="same",  # Keeps the image size the same after applying the filter
        activation="relu",  # Activation function to remove negative values (helps learning)
        input_shape=[
            64,
            64,
            3,
        ],  # Input image size (64x64 pixels, 3 color channels: RGB)
    )
)
# Step 2 - Pooling
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2, padding="valid"))
# Adding a second convolutional layer
cnn.add(
    tf.keras.layers.Conv2D(filters=32, kernel_size=3, padding="same", activation="relu")
)
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2, padding="valid"))
# Step 3 - Flattening
cnn.add(tf.keras.layers.Flatten())
# Step 4 - Full Connection
cnn.add(tf.keras.layers.Dense(units=128, activation="relu"))
# Step 5 - Output Layer
cnn.add(tf.keras.layers.Dense(units=1, activation="sigmoid"))


# Part 3 - Training the CNN
# Compiling the CNN
cnn.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Training the CNN on the Training set and evaluating it on the Test set
cnn.fit(
    training_set,
    steps_per_epoch=len(
        training_set
    ),  # Number of batches per epoch (total dataset size / batch size)
    epochs=25,  # Number of times the model will go through the entire dataset
    validation_data=test_set,  # Dataset used to evaluate the model after each epoch
    validation_steps=len(test_set),  # Number of batches used for validation per epoch
    workers=4,  # Number of CPU cores to use for loading data (speeds up training)
    use_multiprocessing=True,  # Enables parallel data loading for better performance
)


import numpy as np
from tensorflow.keras.preprocessing import image

# Load and preprocess the test image
test_image = image.load_img(
    "deep-leaning/task2-CNN/dataset/single_prediction/cat_or_dog_1.jpg",
    target_size=(64, 64),
)
test_image = image.img_to_array(test_image)  # Convert to NumPy array
test_image = np.expand_dims(test_image, axis=0)  # Expand dimensions for prediction
# Predict using the trained CNN
result = cnn.predict(test_image)
# Get class indices from the training set
class_indices = training_set.class_indices  # {'cats': 0, 'dogs': 1}
class_labels = {v: k for k, v in class_indices.items()}  # Reverse dictionary
# Get the predicted class label
predicted_label = class_labels[
    int(result[0][0] > 0.5)
]  # Thresholding for binary classification
print(f"Predicted: {predicted_label}")
