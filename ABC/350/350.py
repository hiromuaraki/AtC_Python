"""
A問題_Past ABCs・・・解けた
難易度32
問題文の読解が難しい

この問題不親切がすぎる
"""

S = input()
n = int(S[-3:])
if 1 <= n <= 349 and n != 316: print("Yes")
else: print("No")


"""
B問題_Dentist Aoki・・・解けた
難易度45

XORで1→０ 0→1で反転させるのもありか
事前に歯を生やした配列を用意し歯を抜く
"""

# XOR０と１反転解法

N,Q = map(int, input().split())
T = list(map(int, input().split()))
d = [1] * max(T)
for t in T:
  d[t - 1] ^= 1
print(N - d.count(0))

N,Q = map(int, input().split())
T = list(map(int, input().split()))
d = []
for t in T:
  if t not in d:
    d.append(t)
    continue
  d.remove(t)
print(N - len(d))
