"""
背の順になるように
(https://algo-method.com/tasks/6021900cc7f93955)

prefix max
※問題の構造を掴む

順番は固定！！！
直前の身長より低い場合のみ、踏み台分を加算していく
prev - a[i]

Ai + hi ≧ A[i - 1] + h[i - 1]
今の最終身長 ≥ 直前の最終身長

必要な分だけあげる
prefix maximum を維持している
＝最大を維持するのが最善！！
"""

n = int(input())
a = list(map(int, input().split()))

ans = 0
prev = a[0]
for i in range(1, n):
  if a[i] < prev:
    ans += prev - a[i]
  prev = max(prev, a[i])
print(ans)