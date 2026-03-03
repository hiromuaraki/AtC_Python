"""
半分にして行く
(https://algo-method.com/tasks/1276KPdU)
データ構造：ヒープ（二分木）

配列の中から K 回 操作をして、最終的な合計を求める問題です。
配列の中で最大の値を見つけて半分にする操作を K 回行い、最終的な合計を出す。

最終的な合計を最小化したい

Pythonのヒープ：最小ヒープ（min-heap）
-＝負とすることで最大値を取り出すようにしている
"""

import heapq

n,k = map(int, input().split())
a = list(map(int, input().split()))
# Pythonのheapqは最小値しか取り出せないため、予め-1倍し
# -と-をプラスにすることで最大値を取り出せるようにしておく
heap = [-a_i for a_i in a] 

min_val = 0
heapq.heapify(heap)
while k > 0:
  mx_val = -heapq.heappop(heap) # 正の値へ戻す
  mx_val //= 2
  heapq.heappush(heap, -mx_val)
  k -= 1

print(-sum(heap))

# ダメな解法
# 毎回最大を選ぶ必要があるが、最初のソートで固定されているため、
# 要件を満たしていない。このコードは均等に削る。
# 要件は、常に一番大きいものを削る
# cur = 0
# while K > 0:
#   # 最大値を取り出す
#   a[cur] = a[cur] // 2
#   cur = (cur + 1) % n  
#   K -= 1
# print(sum(a))