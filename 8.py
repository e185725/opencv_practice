


import cv2 
import numpy as np 

def max_pooling(img, g=8):
    out = img.copy()

    h,w,C = img.shape

    nh = int(h/g)
    nw = int(w/g)

    for y in range(nh):
        for x in range(nw):
            for c in range(C):
                out[g*y : g*(y+1), g*x : g*(x+1) , c] = np.max(out[g*y:g*(y+1),g*x:g*(x+1),c]).astype(np.int)


    return out

img = cv2.imread("imori.jpg")

out = max_pooling(img)

cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
