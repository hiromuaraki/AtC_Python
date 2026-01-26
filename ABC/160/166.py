"""
B問題_Trick or Treat
入力形式が難しい（癖ある）
入力の境界を理解するのに頭使う
"""

n,k = map(int, input().split())
cnt = [0] * n

for _ in range(k):
  d= int(input())
  a = list(map(int, input().split()))
  for i  in range(d):
    cnt[a[i] - 1] += 1

print(cnt.count(0))


