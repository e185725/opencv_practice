"""
Histogram normalization

ヒストグラム正規化を実装せよ。

ヒストグラムは偏りを持っていることが伺える。 
例えば、0に近い画素が多ければ画像は全体的に暗く、
255に近い画素が多ければ画像は明るくなる。 
ヒストグラムが局所的に偏っていることをダイナミックレンジが狭いなどと表現する。 
そのため画像を人の目に見やすくするために、ヒストグラムを正規化したり平坦化したりなどの処理が必要である。

このヒストグラム正規化は濃度階調変換(gray-scale transformation) と呼ばれ、
[c,d]の画素値を持つ画像を[a,b]のレンジに変換する場合は次式で実現できる。
今回はimori_dark.jpgを[0, 255]のレンジにそれぞれ変換する。
"""


import numpy as np 
import cv2 


def histogram_normalization(img,a = 0 ,b = 255):

        c = img.min()
        d = img.max()

        out = img.copy()

        #out = np.zeros_like(img)
        out = (b-a) / (d-c) * (out - c) + a
        
        out[out < a] = a
        out[out > b] = b
        out = out.astype(np.uint8)
        print(out)
        return out

img = cv2.imread("imori_dark.jpg").astype(np.float)

out = histogram_normalization(img)

cv2.imshow("result",out)
cv2.waitKey(0)
cv2.destroyAllWindows()

