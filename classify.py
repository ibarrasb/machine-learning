import tensorflow as tf

def classify_trucks():
    model = tf.keras.models.Sequential(
        [
            tf.keras.layers.Conv2D(
                16, (3, 3), activation="relu", input_shape=()
            )
        ]
    )