"""
Prewittフィルタ(3x3)を実装せよ。

Prewitt(プレウィット)フィルタはエッジ抽出フィルタの一種であり、
次式で定義される。 これは微分フィルタを3x3に拡大したものである。
"""

import cv2
import numpy as np

# Gray scale
def BGR2GRAY(img):
	b = img[:, :, 0].copy()
	g = img[:, :, 1].copy()
	r = img[:, :, 2].copy()

	# Gray scale
	out = 0.2126 * r + 0.7152 * g + 0.0722 * b
	out = out.astype(np.uint8)

	return out

def prewitt_filter(img,K_size =3):
    if (len(img.shape) == 3):
        H,W,C = img.shape

    else:
        img = np.expand_dims(img,axis = -1)
        H,W,C = img.shape

    
    pad = K_size // 2
    out = np.zeros((H + pad * 2 , W + pad * 2), dtype= np.float)
    out[pad: pad + H , pad : pad + H] = gray.copy().astype(np.float)
    tmp = out.copy()

    out_v = out.copy()
    out_h = out.copy()

    Kv = [[-1.,-1.,-1.] ,[0.,0.,0.] ,[1.,1.,1.]]
    Kh = [[-1.,0.,1.] ,[-1.,0.,1.] ,[-1.,0.,1.]]

    for y in range(H):
        for x in range(W):
            out_v[pad + y , pad + x] = np.sum(Kv * tmp[y:y + K_size,x: x + K_size])
            out_h[pad + y , pad + x] = np.sum(Kh * tmp[y:y + K_size,x: x + K_size])

    out_v = np.clip(out_v,0,255)
    out_h = np.clip(out_h,0,255)

    out_v = out_v[pad : pad + H, pad : pad + W].astype(np.uint8)
    out_h = out_h[pad : pad + H, pad : pad + W].astype(np.uint8)

    return out_v,out_h

img = cv2.imread("imori.jpg").astype(np.float)

# grayscale
gray = BGR2GRAY(img)

# different filtering
out_v, out_h = prewitt_filter(gray, K_size=3)

# Save result

cv2.imshow("result_v", out_v)
cv2.waitKey(0)
cv2.destroyWindow('result_v')

cv2.imshow("result_h", out_h)
cv2.waitKey(0)
cv2.destroyWindow('result_h')
cv2.destroyAllWindows()