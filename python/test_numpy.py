#NumPyは、Pythonで数値計算を効率的に行うためのライブラリ
import numpy as np

tech=np.array([1, 2, 3])
print(tech)

#二次元配列　配列同士の要素数は同じにしないといけないらしい。
tech2=np.array([[1,2,3],[4,5,6]])
print(tech2)
print()

print("■次元変換(ｶｯｺｲｲ")
tech3_1=np.array([1,2,3,4,5,6,7,8])
tech3_2=tech3_1.reshape(2,4)
print(tech3_1)
print(tech3_2)

print(np.array([-1,0,1], dtype=np.float64))


a=np.array([-1,0,1])

print()
print("■配列のデータ属性")
print(a.dtype)
print(a.shape)
print(a.ndim)
print(a.size)
print(a.flat)
print(a.T)

print("")
print("■構築関数")
#arrange(開始値,終了値,刻み)
print(np.arange(0,10,3))

#linspace(開始値,終了値,分割)
print(np.linspace(0,1,5))

#zeros(長さ,長さ...) 最後が要素数?
print(np.zeros((1,3,4))) 
#oness(長さ,長さ...)
print(np.ones((4,3,1))) 

#random.randは、0以上1未満の乱数からなる配列を生成する。
print(np.random.rand(4))
print(np.random.rand(4,4,4))