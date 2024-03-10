import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import glob
import cv2
import pickle

from keras.models import Sequential
from keras.layers import Conv2D, BatchNormalization, MaxPooling2D, Flatten
import os

def save_model(model, filename):
    pickle.dump(model, open(filename, 'wb'))

def load_model(filename):
    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model