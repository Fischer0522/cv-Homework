import cv2
import numpy as np

img = cv2.imread("homework1/test.png")
cv2.imshow("img", img)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

darker_hsv = img_hsv.copy()
darker_hsv[:, :, 2] = 2 * darker_hsv[:, :, 2]
darker_hsv[:, :, 0] = 0.8 * darker_hsv[:, :, 0]
darker_hsv[:, :, 1] = 1.1 * darker_hsv[:, :, 1]
darker_img = cv2.cvtColor(darker_hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("darker", darker_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
