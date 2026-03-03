"""
グループ分け (2)
(https://algo-method.com/tasks/4904d273a9c27b11)

増加部分列の問題

数列を「増加列」に分解するときの最小個数を求める greedy

各xについて
既存のグループのどれかに入れられないか探す
入れられるなら更新
入れられないなら新しくグループを作る
"""

n = int(input())
a = list(map(int, input().split()))
groups = [] # 各グループの現在の最後の値を管理するリスト

for x in a:
  placed = False
  for i in range(len(groups)):
    # そのグループの最後の値より x が大きければ、そのグループに入れられる
    if groups[i] < x:
      # 常に単調増加になるようにしている
      groups[i] = x
      placed = True
      break
  if not placed:
    groups.append(x)
print(len(groups))