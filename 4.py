"""
大津の２値化
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np 
img = cv2.imread('imori.jpg')
gray = 0.2126 * img[:,:, 2] + 0.7152 * img[..., 1] + 0.0722 * img[..., 0]
# plt.hist(gray.ravel(), bins=255, rwidth=0.8, range=(0, 255))
# plt.xlabel('value')
# plt.ylabel('appearance')
# plt.show()

"""
img[..., 1] == img[:,:,1]
出力は一緒
"""

max_sigma = 0
max_t = 0
H, W ,C= img.shape
# determine threshold
for _t in range(1, 256):
	v0 = gray[np.where(gray < _t)]
	m0 = np.mean(v0) if len(v0) > 0 else 0.
	w0 = len(v0) / (H * W)
	v1 = gray[np.where(gray >= _t)]
	m1 = np.mean(v1) if len(v1) > 0 else 0.
	w1 = len(v1) / (H * W)
	sigma = w0 * w1 * ((m0 - m1) ** 2)
	if sigma > max_sigma:
		max_sigma = sigma
		max_t = _t

th = max_t
print("threshold >>", max_t)
img[:,:,0] = np.where(gray < th , 0 ,255)
img[:,:,1] = np.where(gray < th , 0 ,255)
img[:,:,2] = np.where(gray < th , 0 ,255)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
