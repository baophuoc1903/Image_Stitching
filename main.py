# import logging
#
# logging.basicConfig(level=logging.DEBUG,
#                     format="%(asctime)s: %(levelname)s(%(name)s): %(message)s",
#                     datefmt='%Y-%m-%d %H:%M:%S',)
# logger = logging.getLogger(__name__)
# logger.debug("Test")

import sys

sys.path.append("./Panorama")
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import stitch
import utils
import features


def convertResult(img):
    '''Because of your images which were loaded by opencv,
    in order to display the correct output with matplotlib,
    you need to reduce the range of your floating point image from [0,255] to [0,1]
    and converting the image from BGR to RGB:'''
    img = np.array(img, dtype=float) / float(255)
    img = img[:, :, ::-1]
    return img


list_images = utils.loadImages('./Panorama/data/myhouse', resize=0)
# k0, f0 = features.findAndDescribeFeatures(list_images[0], opt='SIFT')
# k1, f1 = features.findAndDescribeFeatures(list_images[1], opt='SIFT')
#
# img0_kp = features.drawKeypoints(list_images[0], k0)
# img1_kp = features.drawKeypoints(list_images[1], k1)
#
# plt_img = np.concatenate((img0_kp, img1_kp), axis=1)
# plt.figure(figsize=(16, 9))
# plt.imshow(convertResult(plt_img))
# plt.show()
#
# mat = features.matchFeatures(f0, f1, ratio=0.6, opt='BF')
# H, matMask = features.generateHomography(list_images[0], list_images[1])
#
# img = features.drawMatches(list_images[0], k0, list_images[1], k1, mat, matMask)
# plt.figure(figsize=(16, 9))
# plt.imshow(convertResult(img))
# plt.show()
#
# pano, non_blend, left_side, right_side = stitch.warpTwoImages(list_images[1], list_images[0], True)
# plt.figure(figsize=(16, 9))
# plt.imshow(convertResult(left_side))
# plt.figure(figsize=(16, 9))
# plt.imshow(convertResult(right_side))
# plt.show()
#
# # if you choose list_images[1] as desination, the output look like this
# _, non_blend2, _, _ = stitch.warpTwoImages(list_images[0], list_images[1], True)
# plt.figure(figsize=(16, 9))
# plt.imshow(convertResult(non_blend2))
# plt.show()
#
# plt.figure(figsize=(16, 9))
# plt.imshow(convertResult(pano))

# plt.show()

panorama = stitch.multiStitching(list_images)
plt.figure(figsize=(16, 9))
plt.imshow(convertResult(panorama))
plt.show()
