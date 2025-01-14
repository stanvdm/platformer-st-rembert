import os, pygame

ASSETS_FOLDER_PATH = 'assets/'

def load_image(path):
    img = pygame.image.load(ASSETS_FOLDER_PATH + path).convert_alpha()
    return img

def load_images(path):
    images = []
    for img_name in sorted(os.listdir(ASSETS_FOLDER_PATH + path)):
        images.append(load_image(path + '/' + img_name))
    return images