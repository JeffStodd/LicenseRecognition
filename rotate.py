import numpy as np
import cv2

image = cv2.imread("result.jpg")

def rotateImage(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  cv2.imshow("Preview", result)
  cv2.imwrite("result.jpg", result)

rotateImage(image, 353)
