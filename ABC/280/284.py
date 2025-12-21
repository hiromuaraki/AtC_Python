"""
A問題_Sequence of Strings
"""

N = int(input())
S = [input() for _ in range(N)]
print(*S[::-1], sep="\n")


"""
B問題_Multi Test Cases・・・解けた
難易度14
"""

T = int(input())
for _ in range(T):
  n = int(input())
  A = map(int, input().split())
  odd_count = 0
  for a in A:
    if a % 2 != 0:
      odd_count += 1
  print(odd_count)


"""
C問題_Count Connected Components・・・解けた
難易度194
(https://atcoder.jp/contests/abc284/tasks/abc284_c)
単純無無グラフの連結成分の個数を数える

グラフ＋BFS／DFSの問題

連結成分の個数はDFS/BFSの開始回数
"""

from collections import deque

N,M = map(int, input().split())
G = [[] for _ in range(N)]
visited = [False] * N

for _ in range(M):
  v,u = map(int, input().split())
  v -= 1; u -= 1
  G[v].append(u)
  G[u].append(v)

def bfs(start):
  visited[start] = True
  que = deque([start])
  while que:
    v = que.popleft()
    for u in G[v]:
      if not visited[u]:
        visited[u] = True
        que.append(u)
        
count = 0
for i in range(N):
  if not visited[i]:
    bfs(i)
    count += 1
print(count)


"""
D問題_Happy New Year 2023・・・解けない（初挑戦）
難易度658

素因数分解

数学×アルゴリズムでキャッチアップする
N以下の素数列挙, 素数判定, 約数列挙, 素因数分解
"""


T = int(input())
for i in range(T):
  N = int(input())
  p = 2
  while p * p <= N:
    if N % p == 0:
      N //= p
      break
    p += 1
  if N % p == 0:
    print(p, N // p)
  else:
    print(int(N**0.5), p) 
