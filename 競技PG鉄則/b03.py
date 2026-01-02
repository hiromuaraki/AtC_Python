"""
B03 - Supermarket 1
難しい

O(N^2)を成立させるための条件
個数管理
・今使っている i, j を一時的に減らす
・残りに k があるか確認

インデックス制約を残す
・j+1 以降だけを見る
・正しいが高速化にならない
"""

from collections import Counter

n = int(input())
a = list(map(int, input().split()))
MAX_NUM = 1000

# i≠j≠kを管理
cnt = Counter(a)

for i in range(n):
  cnt[a[i]] -= 1 # 一時的に除外
  for j in range(i + 1, n):
    cnt[a[j]] -= 1 # 一時的に除外
    need = MAX_NUM - a[i] - a[j]
    if cnt.get(need, 0) > 0:
      print("Yes")
      exit()
    cnt[a[j]] += 1
  cnt[a[i]] += 1

print("No")