"""
MAX-MINフィルタ

MAX-MINフィルタ(3x3)を実装せよ。

MAX-MINフィルタとはフィルタ内の画素の最大値と最小値の差を出力するフィルタであり、
エッジ検出のフィルタの一つである。 
エッジ検出とは画像内の線を検出るすることであり、
このような画像内の情報を抜き出す操作を特徴抽出と呼ぶ。 
エッジ検出では多くの場合、グレースケール画像に対してフィルタリングを行う。
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

# max-min filter
def max_min_filter(img, K_size=3):
	if len(img.shape) == 3:
		H, W, C = img.shape

		## Zero padding
		pad = K_size // 2
		out = np.zeros((H + pad * 2, W + pad * 2, 3), dtype=np.float)
		out[pad: pad + H, pad: pad + W] = img.copy().astype(np.float)
		tmp = out.copy()

		# filtering
		for y in range(H):
			for x in range(W):
				for c in range(3):
					out[pad + y, pad + x, c] = np.max(tmp[y: y + K_size, x: x + K_size, c]) - np.min(tmp[y: y + K_size, x: x + K_size, c])

		out = out[pad: pad + H, pad: pad + W].astype(np.uint8)

	else:
		H, W = img.shape

		## Zero padding
		pad = K_size // 2
		out = np.zeros((H + pad * 2, W + pad * 2), dtype=np.float)
		out[pad: pad + H, pad: pad + W] = img.copy().astype(np.float)
		tmp = out.copy()

		# filtering
		for y in range(H):
			for x in range(W):
				out[pad + y, pad + x] = np.max(tmp[y: y + K_size, x: x + K_size]) - np.min(tmp[y: y + K_size, x: x + K_size])

		out = out[pad: pad + H, pad: pad + W].astype(np.uint8)

	return out


# Read image
img = cv2.imread("imori.jpg").astype(np.float)

# grayscale
gray = BGR2GRAY(img)
print(gray)

# Max-Min filtering
out = max_min_filter(gray, K_size=3)

# Save result
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()





    