"""
Histogram equalization

ヒストグラム平坦化を実装せよ。

ヒストグラム平坦化とはヒストグラムを平坦に変更する操作であり、
上記の平均値や標準偏差などを必要とせず、ヒストグラム値を均衡にする操作である。

これは次式で定義される。 
ただし、S ... 画素値の総数、Zmax ... 画素値の最大値、h(z) ... 濃度zの度数
"""

import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

def histogram_eqalization(img , z_max = 255):
    
    H,W,C = img.shape

    S = H * W * C * 1

    out = img.copy()

    sum_h = 0

    for i in range(1,z_max):
        ind = np.where(img == i)
        sum_h += len(img[ind])
        z_p = z_max / S * sum_h
        out[ind] = z_p

    out = out.astype(np.uint8)

    return out


img = cv2.imread("imori.jpg")

out = histogram_eqalization(img)

plt.hist(out.ravel(), bins=255, rwidth=0.8, range=(0, 255))
plt.show()

# Save result
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()


    
