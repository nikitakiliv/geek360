import tensorflow as tf
from tensorflow import keras
from keras import layers, utils
import matplotlib.pyplot as plt
import os

image_size = (941//3, 263//3)
batch_size = 16

"""train_ds, val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "C:/Projects/hackaton/dataset/",
    validation_split=0.2,
    subset="both",
    seed=1337,
    image_size=image_size,
    batch_size=batch_size,
)"""


train_ds = keras.utils.image_dataset_from_directory(
    directory='C:/Projects/hackaton/dataset/',
    labels='inferred',
    label_mode='categorical',
    batch_size= batch_size,
    image_size=image_size)
validation_ds = keras.utils.image_dataset_from_directory(
    directory='C:/Projects/hackaton/dataset/',
    labels='inferred',
    label_mode='categorical',
    batch_size=batch_size,
    image_size=image_size)

model = keras.applications.Xception(
    weights=None, input_shape=(941//3, 263//3, 3), classes=102)
model.compile(optimizer='rmsprop', loss='categorical_crossentropy')
model.fit(train_ds, epochs=10, validation_data=validation_ds)
model.save('data')




