from scipy.ndimage import convolve
import cv2
import numpy as np
import matplotlib.pyplot as plt


def gauss_ker(l=5, sig=1.):
    """\
    creates gaussian kernel with side length `l` and a sigma of `sig`
    """
    ax = np.linspace(-(l - 1) / 2., (l - 1) / 2., l)
    gauss = np.exp(-0.5 * np.square(ax) / np.square(sig))
    kernel = np.outer(gauss, gauss)
    return kernel / np.sum(kernel)

img = cv2.imread("/Users/nguyenbaophuoc/Downloads/eight.tif", 0)

gaus1 = gauss_ker(5, 0.5)
gaus2 = gauss_ker(5, 0.4)
diff = gaus1 - gaus2

new_img = convolve(img, diff)
plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.subplot(122)

new_img = cv2.normalize(new_img, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
plt.imshow(new_img, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()
