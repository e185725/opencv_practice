#グレースケール化
#r,g,b をそれぞれY = 0.2126 R + 0.7152 G + 0.0722 B
#の式で求められる値に変えることでグレースケール化できる。
#r,g,b = y,y,y


import cv2 
import matplotlib.pyplot as plt 

img = cv2.imread("imori.jpg")

blue = img[:,:,0].copy()
green = img[:,:,1].copy()
red = img[:,:,2].copy()
#type numpy 
#print(type(red))

img[:,:,0] = 0.2126*red + 0.7152*green + 0.0722*blue
img[:,:,1] = 0.2126*red + 0.7152*green + 0.0722*blue
img[:,:,2] = 0.2126*red + 0.7152*green + 0.0722*blue
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
