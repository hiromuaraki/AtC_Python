"""
A問題_A Healthy Breakfast
難易度19

場合分けの問題
"""
S = input()
if S in ("RSM", "RMS", "SRM"): print("Yes")
else: print("No")

"""
B問題_Vertical Reading・・・解けない
難易度78
全探索＋シミュレーション＋部分文字列
"""

S,T = input().split()
N = len(S)
for w in range(N):
  for c in range(w):
    lst = []
    for i in range(c, N, w):
      lst.append(S[i])
    if "".join(lst) == T:
      print("Yes")
      exit()
print("No")   