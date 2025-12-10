'''
10進法から2進法へ変換

例）10の場合→1010
10 % 2 = 0
 10 // 2 = 5
5 % 2 = 1
 5 // 2 = 2
2 % 2 = 0
 2 // 2 = 1
1 % 2 = 1
 1 // 2 = 0・・・ここでループ終了

0101→1010

割った余りを記録
割った商を更新
Nが0になるまで割り続ける
最後に下から順に読む
'''

N = int(input())
ans = ''
while N >= 1:
  if N % 2 == 0: ans += '0'
  if N % 2 == 1: ans += '1'
  N //= 2
print(ans[::-1])


"""
【N進法展開】
8新数→9進数へ変換
"""

N,K = map(int, input().split())

for _ in range(K):
  n = int(str(N), 8)
  res = ""
  if n == 0:
    res = "0"
  while n > 0:
    res = str(n % 9) + res # この書き方なら逆順にせず済む
    n //= 9
  res = res.replace("8", "5")
  N = res
print(N)