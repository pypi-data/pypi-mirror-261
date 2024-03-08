import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np

def plot_image(image, cmap='viridis'):
    if isinstance(image, str):
        img = mpimg.imread(image)
    elif isinstance(image, np.ndarray):
        img = image
    else:
        raise ValueError("Input must be either a file path or a numpy array.")
    
    plt.imshow(img, cmap=cmap)
    plt.axis('off')
    plt.show()