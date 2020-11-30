#HSV変換
"""
HSV変換を実装して、色相Hを反転せよ。

HSV変換とは、
Hue(色相)、
Saturation(彩度)、
Value(明度) 
で色を表現する手法である

Hue ...
 色合いを0~360度で表現し、赤や青など色の種類を示す。
 ( 0 <= H < 360) 色相は次の色に対応する。

    赤 黄色  緑  水色  青  紫   赤
    0  60  120  180 240 300 360

Saturation ... 
 色の鮮やかさ。Saturationが低いと灰色さが顕著になり、
 くすんだ色となる。 ( 0<= S < 1)

Value ... 
 色の明るさ。
 Valueが高いほど白に近く、
 Valueが低いほど黒に近くなる。 ( 0 <= V < 1)
"""

"""
RGB -> HSV変換は以下の式で定義される。

R,G,Bが[0, 1]の範囲にあるとする。

Max = max(R,G,B)
Min = min(R,G,B)

H =  { 0                            (if Min=Max)
       60 x (G-R) / (Max-Min) + 60  (if Min=B)
       60 x (B-G) / (Max-Min) + 180 (if Min=R)
       60 x (R-B) / (Max-Min) + 300 (if Min=G)
       
V = Max

S = Max - Min
"""

"""
HSV -> RGB変換は以下の式で定義される。

C = S

H' = H / 60

X = C (1 - |H' mod 2 - 1|)

(R,G,B) = (V - C) (1,1,1) + { (0, 0, 0)  (if H is undefined)
                              (C, X, 0)  (if 0 <= H' < 1)
                              (X, C, 0)  (if 1 <= H' < 2)
                              (0, C, X)  (if 2 <= H' < 3)
                              (0, X, C)  (if 3 <= H' < 4)
                              (X, 0, C)  (if 4 <= H' < 5)
                              (C, 0, X)  (if 5 <= H' < 6)

"""
