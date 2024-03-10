import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import glob
import cv2
import pickle

from keras.models import Sequential
from keras.layers import Conv2D, BatchNormalization, MaxPooling2D, Flatten
import os

def load_dataset(image_dir, mask_dir, SIZE):
    train_images = []
    for directory_path in glob.glob(image_dir):
        for img_path in glob.glob(os.path.join(directory_path, "*.tif")) + glob.glob(
                os.path.join(directory_path, "*.png")):
            img = cv2.imread(img_path, cv2.IMREAD_COLOR)
            img = cv2.resize(img, (SIZE, SIZE))
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            train_images.append(img)

    train_images = np.array(train_images)

    train_masks = []
    for directory_path in glob.glob(mask_dir):
        for mask_path in glob.glob(os.path.join(directory_path, "*.tif")) + glob.glob(
                os.path.join(directory_path, "*.png")):
            mask = cv2.imread(mask_path, 0)
            mask = cv2.resize(mask, (SIZE, SIZE))
            train_masks.append(mask)

    train_masks = np.array(train_masks)

    return train_images, train_masks