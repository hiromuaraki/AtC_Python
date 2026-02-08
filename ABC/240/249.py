"""
A問題_Jogging
(https://atcoder.jp/contests/abc249/tasks/abc249_a)
周期＋シミュレーション
結構難しい

・何回繰り返すか
・何秒余るか

A＋C秒の周期
D＋F秒の周期
"""


a,b,c,d,e,f,x = map(int, input().split())

# シミュレーション
taka_, ao = 0, 0
for k in range(x):
  if k % (a + c) < a: taka_+= b
  if k % (d + f) < d: ao += e

if taka_ == ao: print("Draw")
elif taka_ > ao: print("Takahashi")
else: print("Aoki")

# 周期の解法
def cycle(x, t, k, s):
  q = x // (t + k) # x秒の間に何回繰り返すか
  r = x % (t + k) # 何秒余るか
  if r <= t: return (t * q + r) * s
  else: return (t * q + t) * s

taka = cycle(x, a, c, b) 
aoki = cycle(x, d, f, e)
ans = ""
if taka == aoki: ans ="Draw"
elif taka > aoki: ans = "Takahashi"
else: ans = "Aoki"
print(ans)