"""
LoGフィルタ(sigma=3、カーネルサイズ=5)を実装し、
imori_noise.jpgのエッジを検出せよ。

LoGフィルタとはLaplacian of Gaussianであり、
ガウシアンフィルタで画像を平滑化した後にラプラシアンフィルタで輪郭を取り出すフィルタである。

Laplcianフィルタは二次微分をとるのでノイズが強調されるのを防ぐために、
予めGaussianフィルタでノイズを抑える。LoGフィルタは次式で定義される。

ラプラシアンを∇^2、ガウシアンフィルタをG、画像をIとする。
次式によって、ガウシアンフィルタリング後にラプラシアンフィルタする操作を、
ガウシアンフィルタをラプラシアンしたものでフィルタリングする操作に置き換えることが可能。
"""

import cv2 
import numpy as np 

def BGR2GRAY(img):
	b = img[:, :, 0].copy()
	g = img[:, :, 1].copy()
	r = img[:, :, 2].copy()

	# Gray scale
	out = 0.2126 * r + 0.7152 * g + 0.0722 * b
	out = out.astype(np.uint8)

	return out

def LoG_filter(img,K_size = 5,sigma = 3):
    if (len(img.shape) == 3):
        H,W,C = img.shape

    else:
        H,W = img.shape

    #zero padding
    pad = K_size // 2
    out = np.zeros((H + pad * 2, W + pad * 2), dtype = np.float)
    out[pad: pad + H, pad: pad + W] = gray.copy().astype(np.float)
    tmp = out.copy()

    #log kernel 
    K = np.zeros((K_size,K_size) , dtype= np.float)
    for x in range(-pad,-pad + K_size):
        for y in range(-pad,-pad+K_size):
            K[y + pad, x + pad ] = (x ** 2 + y ** 2 - 2 * (sigma ** 2)) * np.exp( - (x ** 2 + y **2 ) / (2 * (sigma ** 2)))

    K /= (2 * np.pi * (sigma ** 6))
    K /= K.sum()


    """
	K =                 np.array([[0, 0, 1, 0, 0],
								[0, 1, 2, 1, 0],
								[1, 2, -16, 2, 1],
								[0, 1, 2, 1, 0],
								[0, 0, 1, 0, 0]])
    """

    for y in range(H):
        for x in range(W):
            out[pad + y , pad + x] = np.sum(K * tmp[y: y + K_size, x:x +K_size])
        
    out = np.clip(out,0,255)
    out = out[pad: pad + H, pad: pad+ W].astype(np.uint8)

    return out

img = cv2.imread("imori_noise.jpg")

# grayscale
gray = BGR2GRAY(img)

# LoG filtering
out = LoG_filter(gray, K_size=5, sigma=3)

# Save result

cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()





