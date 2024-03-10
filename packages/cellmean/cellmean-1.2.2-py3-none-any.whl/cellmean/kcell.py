import os
from skimage import io
from sklearn.cluster import KMeans
import numpy as np

def cell_segment(image, num_clusters=4):
    if isinstance(image, str):  
        image = io.imread(image)
    elif not isinstance(image, np.ndarray):
        raise ValueError("Input must be either a file path or a numpy array.")
        
    w, h, d = original_shape = tuple(image.shape)
    image_2d = np.reshape(image, (w * h, d))
    kmeans = KMeans(n_clusters=num_clusters, n_init=10)
    kmeans.fit(image_2d)
    labels = kmeans.predict(image_2d)
    segmented_image = np.reshape(labels, (w, h))
    return segmented_image