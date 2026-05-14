"""
箱の中の箱
(https://algo-method.com/tasks/415)
N個の箱の中からXの箱を取り出すにはいくつの箱を開ける必要があるか？
"""
N,X = map(int, input().split())
A = list(map(int, input().split()))
A.insert(0, -1)
res = 0

while X != 0:
    res += 1
    X = A[X]
print(res)