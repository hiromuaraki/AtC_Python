"""
【データ構造】
set, map
"""

N = int(input())
S = [input() for _ in range(N)]

ans = set()
for i in range(N):
    if S[i] not in ans:
      ans.add(i + 1)
      print(i + 1)