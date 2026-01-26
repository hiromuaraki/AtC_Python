"""
B問題_Vacation Together
(https://atcoder.jp/contests/abc311/tasks/abc311_b)

実装重い
グリッドを論理的配列に変換
連続区間の問題
"""

n,d = map(int, input().split())
s = [input() for _ in range(n)]
free = [False] * d
for j in range(d):
  is_free = True
  for i in range(n):
    if s[i][j] == "x":
      is_free = False
      break
  if is_free:
    free[j] = is_free

# コーナーケース処理
# 暇な日が1もない場合
if free.count(True) == 0:
  print(0)
  exit()

ans = 1
count = 1
for i in range(d - 1):
  if free[i] and free[i + 1]:
    count += 1
  else:
    count = 1
  ans = max(ans, count)
print(ans)


