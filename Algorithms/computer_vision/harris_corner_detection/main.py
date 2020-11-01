"""
Computer Vision:

Computer vision is a field of computer science that works on enabling computers to see, identify and process images in the same way that human vision does, and then provide appropriate output. It is like imparting human intelligence and instincts to a computer. Image processing and computer vision and little different from each other.Image processing means applying some algorithms for transforming image from one form to other like smoothing,contrasting, stretching etc While in computer vision comes from modelling image processing using the techniques of machine learning.Computer vision applies machine learning to recognize patterns for interpretation of images. Much like the process of visual reasoning of human vision
"""

import cv2
import numpy as np


# Harris Corner Detector
# https://en.wikipedia.org/wiki/Harris_Corner_Detector

class Harris_Corner:
    def __init__(self, k: float, window_size: int):

        """
        k : is an empirically determined constant in [0.04,0.06]
        window_size : neighbourhoods considered
        """

        if k in (0.04, 0.06):
            self.k = k
            self.window_size = window_size
        else:
            raise ValueError("invalid k value")

    def __str__(self):

        return f"Harris Corner  detection with k : {self.k}"

    def detect(self, img_path: str):

        """
        Returns the image with corners identified
        img_path  : path of the image
        output : list of the corner positions, image
        """

        img = cv2.imread(img_path, 0)
        h, w = img.shape
        corner_list = []
        color_img = img.copy()
        color_img = cv2.cvtColor(color_img, cv2.COLOR_GRAY2RGB)
        dy, dx = np.gradient(img)
        ixx = dx ** 2
        iyy = dy ** 2
        ixy = dx * dy
        k = 0.04
        offset = self.window_size // 2
        for y in range(offset, h - offset):
            for x in range(offset, w - offset):
                wxx = ixx[
                    y - offset : y + offset + 1, x - offset : x + offset + 1
                ].sum()
                wyy = iyy[
                    y - offset : y + offset + 1, x - offset : x + offset + 1
                ].sum()
                wxy = ixy[
                    y - offset : y + offset + 1, x - offset : x + offset + 1
                ].sum()

                det = (wxx * wyy) - (wxy ** 2)
                trace = wxx + wyy
                r = det - k * (trace ** 2)
                # Can change the value
                if r > 0.5:
                    corner_list.append([x, y, r])
                    color_img.itemset((y, x, 0), 0)
                    color_img.itemset((y, x, 1), 0)
                    color_img.itemset((y, x, 2), 255)
        return color_img, corner_list


if __name__ == "__main__":

    edge_detect = Harris_Corner(0.04, 3)
    color_img, _ = edge_detect.detect("test3.jpg")
    cv2.imwrite("detect.png", color_img)
