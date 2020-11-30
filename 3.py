"""
Q.3. 二値化

画像を二値化せよ。 
二値化とは、画像を黒と白の二値で表現する方法である。 
ここでは、グレースケールにおいて閾値を128に設定し、
下式で二値化する。

y = { 0 (if y < 128)
     255 (else) 
"""

import cv2 
import numpy as np 
img = cv2.imread("imori.jpg")

blue = img[:,:,0].copy()
green = img[:,:,1].copy()
red = img[:,:,2].copy()

y = 0.2126*red + 0.7152*green + 0.0722*blue

img[:,:,0] = np.where(y < 128 , 0 ,255)
img[:,:,1] = np.where(y < 128 , 0 ,255)
img[:,:,2] = np.where(y < 128 , 0 ,255)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()