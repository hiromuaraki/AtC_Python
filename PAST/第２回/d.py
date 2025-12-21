"""
全探索・・・解けない（要復習）

計算量：O(N^3)
Sのi文字目＝|S-|T|+1通り

英小文字＝26通り
”.”＝１通り
26＋１＝27通り
27^3+27^2+27^1=27^6通り
"""

# Sのi文字目から始まる部分がTとマッチするかどうかを調べる
def is_math(T, S):
  for i in range(len(S)-len(T)+1):
    ok=True
    for j in range(len(T)):
      if S[i+j] != T[j] and T[j] != ".":
        ok=False
    if ok:
      return True
  
  return False


S=input()
C="abcdefghijklmnopqrstuvwxyz." # 27通り
# 文字列Sとマッチする配列
M=[]

# 長さ1の文字列を調べSとマッチするものをMに入れる
for T in C:
  if is_math(T, S):
    M.append(T)

# 長さ2の文字列を調べSとマッチするものをMに入れる
for c1 in C:
  for c2 in C:
    T=c1+c2
    if is_math(T, S):
      M.append(T)

# 長さ3の文字列を調べSとマッチするものをMに入れる
for c1 in C:
  for c2 in C:
    for c3 in C:
      T=c1+c2+c3
      if is_math(T, S):
        M.append(T)

print(len(M))