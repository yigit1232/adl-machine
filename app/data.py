import os
from core.settings import BASE_DIR
def get_images():
    PATH = rf"{BASE_DIR}\static\images\product"
    images = os.listdir(PATH)
    return images
