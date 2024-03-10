import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import glob
import cv2
import pickle

from keras.models import Sequential
from keras.layers import Conv2D, BatchNormalization, MaxPooling2D, Flatten
import os


def build_extractor(size, enable_more_layers=False):
    activation = 'sigmoid'
    feature_extractor = Sequential()
    feature_extractor.add(Conv2D(32, 3, activation=activation, padding='same', input_shape=(size, size, 3)))
    feature_extractor.add(Conv2D(32, 3, activation=activation, padding='same', kernel_initializer='he_uniform'))

    if enable_more_layers:
        feature_extractor.add(Conv2D(64, 3, activation=activation, padding='same', kernel_initializer='he_uniform'))
        feature_extractor.add(BatchNormalization())
        #
        feature_extractor.add(Conv2D(64, 3, activation=activation, padding='same', kernel_initializer='he_uniform'))
        feature_extractor.add(BatchNormalization())
        feature_extractor.add(MaxPooling2D())
        feature_extractor.add(Flatten())

    return feature_extractor

def extract_features(feature_extractor, X_train, y_train):
    X = feature_extractor.predict(X_train)
    X = X.reshape(-1, X.shape[3])
    Y = y_train.reshape(-1)
    return X, Y

def rf_dataset(X, Y):
    dataset = pd.DataFrame(X)
    dataset['Label'] = Y
    print(dataset['Label'].unique())
    print(dataset['Label'].value_counts())

    # If we do not want to include pixels with value 0
    # e.g. Sometimes unlabeled pixels may be given a value 0.
    dataset = dataset[dataset['Label'] != 0]

    X_for_RF = dataset.drop(labels=['Label'], axis=1)
    Y_for_RF = dataset['Label']
    
    return X_for_RF, Y_for_RF

from sklearn.ensemble import RandomForestClassifier

def train_random_forest(X, Y):
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X, Y)
    return model



