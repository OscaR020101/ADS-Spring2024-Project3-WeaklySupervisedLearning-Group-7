import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Activation


def build_model_I():
    model = Sequential([
        # Convolutional Layer 1: 32 filters, 3x3 kernel, input shape 32x32x3
        Conv2D(32, (3, 3), padding='same', input_shape=(32, 32, 3)),
        Activation('relu'),

        # Pooling Layer 1: 2x2 pool size
        MaxPooling2D(pool_size=(2, 2)),

        # Convolutional Layer 2: 64 filters
        Conv2D(64, (3, 3), padding='same'),
        Activation('relu'),

        # Pooling Layer 2
        MaxPooling2D(pool_size=(2, 2)),

        # Flatten the output to feed into the Dense layer
        Flatten(),

        # Fully Connected Layer
        Dense(64),
        Activation('relu'),

        # Output Layer: 10 classes
        Dense(10),
        Activation('softmax')
    ])

    return model


# write your code here...

def model_I(image):
    '''
    This function should takes in the image of dimension 32*32*3 as input and returns a label prediction
    '''
    # write your code here...
    # Load the trained Model I
    model = build_model_I()
    # Assuming the model weights are loaded here

    # Preprocess the image to fit the model input format
    image = image.reshape((1, 32, 32, 3)) / 255.0  # Normalize the image

    # Predict the class
    prediction = model.predict(image)

    # Convert prediction to class label
    label = np.argmax(prediction, axis=1)

    return label