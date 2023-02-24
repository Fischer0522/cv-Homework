import cv2
import numpy as np

img = cv2.imread("homework1/test.png")
cv2.imshow("img", img)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lighter_hsv = img_hsv.copy()
lighter_hsv[:, :, 2] = 2 * lighter_hsv[:, :, 2]
lighter_hsv[:, :, 0] = 0.8 * lighter_hsv[:, :, 0]
lighter_hsv[:, :, 1] = 1.1 * lighter_hsv[:, :, 1]
darker_img = cv2.cvtColor(lighter_hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("darker", darker_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
