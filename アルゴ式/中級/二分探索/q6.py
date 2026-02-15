"""
何番目の重さ？
(https://algo-method.com/tasks/399)

lower_bound：Ax < Aiにいくつあるか
left = a_i未満の要素がちょうどleft個ある位置
right = まだ答えが含まれている可能性のある右端

left == rightになった時点で left < a_i未満の要素数が確定

left = mid + 1
midは確実に条件を満たす側、midを含めて捨てる
→左は全部答えではない＝mid以前は全て探索済み

right = mid
midは境界候補、midを含めて残す
"""
import bisect
n = int(input())
a = list(map(int, input().split()))
w = sorted(a) # 元データはソートしない


# Ai >= w[i]になる位置を探す
# x を壊さずに挿入できる一番左の位置
for i in range(n):
  print(bisect.bisect_left(w, a[i]))

# 二分探索
for a_i in a:
  left = 0
  right = n
  # 答えが見つかるまで探す
  # 答えはleft以上、right未満の範囲 [left, right) ※半開区間
  while right != left:
    mid = (left + right) // 2
    # a_i未満の要素がwにいくつあるかを数えている
    if w[mid] < a_i:
      left = mid + 1
    else:
      right = mid
  print(left)

# マッピング＋ソート
b = {a_i : i for i, a_i in enumerate(sorted(a))}
for a_i in a:
  print(b[a_i])


  


