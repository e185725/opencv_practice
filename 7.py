"""
ここでは画像をグリッド分割(ある固定長の領域に分ける)し、
かく領域内(セル)の平均値でその領域内の値を埋める。 
このようにグリッド分割し、その領域内の代表値を求める操作はPooling(プーリング) と呼ばれる。
これらプーリング操作はCNN(Convolutional Neural Network) において重要な役割を持つ。

これは次式で定義される。ここでいうRはプーリングを行う領域である。
つまり、3x3の領域でプーリングを行う。|R|=3x3=9となる。
"""

import cv2 
import numpy as np 

def average_pooling(img, g=8):
    out = img.copy()

    h,w,C = img.shape

    nh = int(h/g)
    nw = int(w/g)

    for y in range(nh):
        for x in range(nw):
            for c in range(C):
                out[g*y : g*(y+1), g*x : g*(x+1) , c] = np.mean(out[g*y:g*(y+1),g*x:g*(x+1),c]).astype(np.int)


    return out

img = cv2.imread("imori.jpg")

out = average_pooling(img)

cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
