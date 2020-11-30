"""
ガウシアンフィルタ(3x3、標準偏差1.3)を実装し、
imori_noise.jpgのノイズを除去せよ。

ガウシアンフィルタとは画像の平滑化（滑らかにする）
を行うフィルタの一種であり、
ノイズ除去にも使われる。

ノイズ除去には他にも、メディアンフィルタ(Q.10)、
平滑化フィルタ(Q.11)、LoGフィルタ(Q.19)などがある。

ガウシアンフィルタは注目画素の周辺画素を、
ガウス分布による重み付けで平滑化し、次式で定義される。
このような重みはカーネルやフィルタと呼ばれる。

ただし、画像の端はこのままではフィルタリングできないため、
画素が足りない部分は0で埋める。これを0パディングと呼ぶ。 
かつ、重みは正規化する。(sum g = 1)

重みはガウス分布から次式になる。

g(x,y,s) = 1/ (2 * pi * sigma * sigma) * exp( - (x^2 + y^2) / (2*s^2))
"""

import cv2 
import numpy as np 

def gaussian_filter(img, K_size=3, sigma=1.3):

    if (len(img.shape) == 3):
        H,W,C = img.shape

    else:
        img = np.expand_dims(img,axis=-1)
        H,W,C = img.shape

    pad = K_size // 2
    out = np.zeros((H + pad * 2 , W + pad * 2 , C), dtype = np.float)
    out[pad:pad + H, pad : pad + W] = img.copy().astype(np.float)

    K = np.zeros((K_size,K_size), dtype = np.float)

    for x in range(-pad,-pad + K_size):
        for y in range(-pad,-pad + K_size):
            K[y + pad,x + pad] = np.exp( -(x ** 2 + y ** 2) / (2 * (sigma ** 2)) )
    
    K /= (2 * np.pi * sigma * sigma)
    K /= K.sum()

    tmp = out.copy()

    for y in range(H):
        for x in range(W):
            for c in range(C):
                out[pad + y,pad + x, c] = np.sum(K * tmp[y:y + K_size, x:x + K_size,c])

    
    out = np.clip(out,0,255)
    out = out[pad: pad + H, pad : pad + W].astype(np.uint8)

    return out 


img = cv2.imread("imori_noise.jpg")

out = gaussian_filter(img, K_size=3, sigma=1.3)

cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()

