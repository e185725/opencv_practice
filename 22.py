"""
ヒストグラムの平均値をm0=128、
標準偏差をs0=52になるように操作せよ。

これはヒストグラムのダイナミックレンジを変更するのではなく、
ヒストグラムを平坦に変更する操作である。

平均値m、標準偏差s、のヒストグラムを平均値m0, 
標準偏差s0に変更するには、次式によって変換する。
"""
import cv2 
import numpy as np 
import matplotlib.pyplot as plt

def hist_mani(img , m0 = 128 , s0 = 52):

        m = np.mean(img)
        s = np.std(img)

        out = img.copy()

        out = s0/s * (  out - m) + m0

        out = out.astype(np.uint8)

        return out
        


img = cv2.imread("imori_dark.jpg")

out = hist_mani(img)


cv2.imshow("result",out)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.hist(out.ravel(),bins = 255, rwidth = 0.8 , range= (0,255))
plt.show()
