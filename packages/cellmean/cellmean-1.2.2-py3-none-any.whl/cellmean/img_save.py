from PIL import Image
import os
import numpy as np

def img_save(image, save_path='.', image_path=None, k=None):
    if image_path is not None:
        filename = os.path.basename(image_path)
    else:
        filename = 'img_k.jpg'
        
    if k is not None:
        save_name = os.path.join(save_path, f'img_{k}.jpg')
    else:
        save_name = os.path.join(save_path, filename)
    
    image_normalized = (image / np.max(image) * 255).astype(np.uint8)
    pil_image = Image.fromarray(image_normalized)
    pil_image.save(save_name)