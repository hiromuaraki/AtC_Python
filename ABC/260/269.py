"""
A問題_Anyway Takahashi
"""

a,b,c,d = map(int, input().split())
print((a + b) * (c - d), "Takahashi", sep="\n")


"""
B問題_Rectangle Detection・・・解けた
難易度68

グリッド＆全探索
頭を使う
"""

S = [input() for _ in range(10)]

grid = []
for i in range(10):
  for j in range(10):
    if S[i][j] == ".": continue
    grid.append((i + 1 , j + 1))

for x,y in zip(grid[0], grid[-1]):
  print(x, y)


"""
C問題_Submask・・・解けない
難易度384
(https://atcoder.jp/contests/abc269/tasks/abc269_c)

ビット全探索：(https://drken1215.hatenablog.com/entry/2019/12/14/171657)
ビット演算：(https://qiita.com/drken/items/7c6ff2aa4d8fce1c9361)
部分集合の列挙

部分集合列挙の書き方
S = (S - 1) & N
整数値SはNの部分集合を表す

空集合の時は探索しない
"""

N = int(input())
S = N
ans = set() # 重複を除く

while S:
  S = (S - 1) & N
  # 部分集合を追加
  ans.add(S)
# N自身を末尾に追加
ans.add(N)
ans = sorted(ans)
print(*ans, sep="\n") 

