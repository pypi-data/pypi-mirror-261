import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import glob
import cv2
import pickle

from keras.models import Sequential
from keras.layers import Conv2D, BatchNormalization, MaxPooling2D, Flatten
import os

def inference_image(image_path, feature_extractor, SIZE):
    test_img = cv2.imread(image_path, cv2.IMREAD_COLOR)       
    test_img = cv2.resize(test_img, (SIZE, SIZE))
    test_img = cv2.cvtColor(test_img, cv2.COLOR_RGB2BGR)
    test_img = np.expand_dims(test_img, axis=0)

    X_test_feature = feature_extractor.predict(test_img)
    X_test_feature = X_test_feature.reshape(-1, X_test_feature.shape[3])
    
    return X_test_feature

def visualize_image(prediction_model, feature_vector, mask_shape):
    prediction = prediction_model.predict(feature_vector)
    prediction_image = prediction.reshape(mask_shape)
    plt.imshow(prediction_image, cmap='gray')
    plt.show()