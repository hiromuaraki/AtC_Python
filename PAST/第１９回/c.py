"""
全探索・・・解けない
prev = 元のiを保持
0-9桁に先頭から順に書き換える

1桁を変更して「隣り合う桁の差が1以内」になる数が作れるか？

1桁ずつ全探索して、
すべての桁の差が1以下かを確認
"""

S = list(map(int, input()))

for i in range(len(S)):
  prev = S[i]
  for j in range(10):
    if i == 0 and j == 0:
      continue
    ok = True
    S[i] = j
    for k in range(1, len(S)):
      if abs(S[k] - S[k - 1]) > 1:
        ok = False
        break
    if ok:
      print("Yes")
      exit()
    S[i] = prev
print("No")