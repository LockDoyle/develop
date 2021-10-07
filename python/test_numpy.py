#NumPyは、Pythonで数値計算を効率的に行うためのライブラリ
import numpy as np

tech=np.array([1, 2, 3])
print(tech)

#二次元配列　配列同士の要素数は同じにしないといけないらしい。
tech2=np.array([[1,2,3],[4,5,6]])
print(tech2)


print(np.array([-1,0,1], dtype=np.float64))


a=np.array([-1,0,1])


print("配列のデータ属性")
print(a.dtype)
print(a.shape)
print(a.ndim)
print(a.size)
print(a.flat)
print(a.T)

print("")
print("構築関数")
print(np.arange(0,10,2))