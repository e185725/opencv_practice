
#5実装

import cv2 
import numpy as np 

img = cv2.imread("imori.jpg") / 255.
#bgr2hsv
hsv = np.zeros_like(img,dtype = np.float32)
print(hsv)

max_v = np.max(img, axis=2).copy()
min_v = np.min(img, axis=2).copy()
min_arg = np.argmin(img, axis=2)
#min_arg は最小値を返すインデックスを返す
print(min_arg)
print(img.shape)
#h
hsv[:,:,0][np.where( max_v == min_v )] = 0
## if min == B
index = np.where(min_arg == 0)
hsv[:,:,0][index] = 60* (img[...,1][index] - img[...,2][index]) / (max_v[index] - min_v[index]) + 60
## if min == R
ind = np.where(min_arg == 2)
hsv[..., 0][ind] = 60 * (img[..., 0][ind] - img[..., 1][ind]) / (max_v[ind] - min_v[ind]) + 180
## if min == G
ind = np.where(min_arg == 1)
hsv[..., 0][ind] = 60 * (img[..., 2][ind] - img[..., 0][ind]) / (max_v[ind] - min_v[ind]) + 300
		
# S
hsv[..., 1] = max_v.copy() - min_v.copy()

# V
hsv[..., 2] = max_v.copy()

print(hsv)
#-------
#hsv2bgr

hsv[..., 0] = (hsv[..., 0] + 180) % 360

h = hsv[...,0]
s = hsv[...,1]
v = hsv[...,2]

c = s
h_ = h / 60.
x = c * (1 - np.abs(h_ % 2 - 1))
z = np.zeros_like(h)

val = [[z,x,c],[z,c,x],[x,c,z],[c,x,z],[c,z,x],[x,z,c]]

for i in range(len(val)):
    ind = np.where((i <= h_) & (h_ < (i+1)))
    hsv[...,0][ind] = (v-c)[ind] + val[i][0][ind]
    hsv[...,1][ind] = (v-c)[ind] + val[i][1][ind]
    hsv[...,2][ind] = (v-c)[ind] + val[i][2][ind]

hsv[np.where(max_v == min_v)] = 0
hsv = np.clip(hsv,0,1)
hsv = (hsv * 255).astype(np.uint8)



cv2.imshow("result", hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

