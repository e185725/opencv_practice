"""
Q.6. 減色処理

ここでは画像の値を256^3から4^3、すなわち
R,G,B in {32, 96, 160, 224}の各4値に減色せよ。 
これは量子化操作である。 各値に関して、以下の様に定義する。

val = {  32  (  0 <= val <  64)
         96  ( 64 <= val < 128)
        160  (128 <= val < 192)
        224  (192 <= val < 256)

"""
import cv2
import numpy as np
img = cv2.imread("imori.jpg")

def color_level_down(_img):
    img = _img.copy()
    out = np.zeros_like(img)
    
    out = np.where( (img >= 192) & (img < 256), 224 , out)
    out = np.where( (img >= 128) & (img < 192), 160 , out)
    out = np.where( (img >= 192) & (img < 128), 96 , out)
    out = np.where( (img >= 0  ) & (img < 64 ), 32 , out)

    #out = out // 64 * 64 + 32 これが圧倒的に楽
    print(out)
    return out

out = color_level_down(img)

cv2.imshow("img",out)
cv2.waitKey(0)
cv2.destroyAllWindows()


