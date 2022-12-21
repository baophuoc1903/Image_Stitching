import sys

sys.path.append("Images")
import numpy as np
import matplotlib.pyplot as plt
import stitch
import utils


def convertResult(img):
    img = np.array(img, dtype=float) / float(255)

    return img[:, :, ::-1]


if __name__ == '__main__':
    list_images = utils.loadImages('Images', resize=0)
    panorama = stitch.multiStitching(list_images)
    plt.figure(figsize=(10, 5))
    plt.imshow(convertResult(panorama))
    plt.show()
