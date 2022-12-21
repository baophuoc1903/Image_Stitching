import cv2
from imutils import paths


def loadImages(path, resize):
    """Load Images from path to array, @param path is the folder which containing images, @param resize is True
    if image is halved in size, otherwise is False"""
    image_path = list(paths.list_images(path))
    image_path.sort()
    list_image = []
    for _, j in enumerate(image_path):
        image = cv2.imread(j)
        if resize == 1:
            image = cv2.resize(
                image, (int(image.shape[1] / 4), int(image.shape[0] / 4))
            )
        list_image.append(image)
    return list_image


if __name__ == '__main__':
    lst = loadImages('Images', resize=0)
    print(len(lst))
