import numpy as np
import tensorflow as tf
import os
from tensorflow import keras
from keras import layers
import cv2
import warnings
from keras.models import Sequential
from keras.layers import Activation, Dense, Flatten, BatchNormalization, Conv2D, MaxPool2D, Dropout
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ReduceLROnPlateau
from keras.callbacks import ModelCheckpoint, EarlyStopping
warnings.simplefilter(action='ignore', category=FutureWarning)

model = Sequential()
#max[0,input] :relu fct after each conv
model.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu', input_shape=(64,64,1)))
model.add(MaxPool2D(pool_size=(2, 2), strides=2))

model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu', padding = 'same'))
model.add(MaxPool2D(pool_size=(2, 2), strides=2))

#convert the data into a 1-dimensional array because dense layer takes a vector as input
model.add(Flatten())
model.add(Dense(64,activation ="relu"))
#convert class score to classe probability:softmax
model.add(Dense(10,activation ="softmax"))





