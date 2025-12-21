"""
A問題_Too Many Requests
"""

N,M = map(int, input().split())
for i in range(N):
  if i < M:
    print("OK")
    continue
  print("Too Many Requests ")


"""
B問題_N - 1・・・解けた
難易度24
"""

N,M = map(int, input().split())
A = list(map(int, input().split()))
total = sum(A)
print("Yes" if total - M in A else "No")


"""
C問題_Odd One Subsequence・・・解けた
難易度201 3Q
(https://atcoder.jp/contests/abc429/tasks/abc429_c)

組合せの問題

・頻度分布を取る
・nC2個選ぶ数と残りの数を求める
・残りの数 = nC2 - N - nC2で求められる

N個の中から2個選ぶ＝nC2個が数列の種類分ある
nC2個 = N * (N - 1) // 2

それぞれの組の分布を取る
例）3 2 5 2 2 3
＜分布（組）＞
2: 3
3: 1
5: 1

n個の中から2個選ぶ＊全体 - 1個の組の数を引いたものの総和

→2つ選ぶ＋異なる値をつ選ぶ組わせの総数
"""

from collections import Counter

N= int(input())
A = list(map(int, input().split()))
counter = Counter(A)
ans = 0
for count in counter.values():
  ans += count * (count - 1)//2 * (N - count)

print(ans)