
import cv2 
import matplotlib.pyplot as plt 

img = cv2.imread("imori.jpg")
"""
imgの成分
[ [[1,1,1],[0,0,0],[2,2,2]] ],
[ [[3,3,3],[4,4,4],[5,5,5]] ],
[ [[6,6,6],[2,2,2],[1,1,1]] ]

のようになっている上記は３＊３の画像を読み込んだと仮定している。

それぞれの成分をとるとき...
img[y,x,0=b,1=g,2=r]となっている
"""
blue = img[:,:,0].copy()
green = img[:,:,1].copy()
red = img[:,:,2].copy()

img[:,:,0] = red
img[:,:,2] = blue

#print(img[:,:,2])

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

