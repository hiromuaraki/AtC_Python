"""
B問題_Balance
難易度6Q
少し難しい
(https://atcoder.jp/contests/abc129/tasks/abc129_b)

最初問題文の意味がよくわからなかったが、
つまるところ, 重りの番号以下とより大きい重りを2つのグループに分け総和した絶対値の差を求めるということ
が問題文に書いてあること。
i = 重りの番号のため制約通り+1が必要がある点だけ注意
"""

n = int(input())
w = list(map(int, input().split()))

min_diff = 10**9
for t in range(1, n):
  s1, s2 = 0, 0
  for i, w_i in enumerate(w):
    if i + 1 <= t:
      s1 += w_i
    else:
      s2 += w_i
  min_diff = min(min_diff, abs(s1 - s2))
print(min_diff)
  
