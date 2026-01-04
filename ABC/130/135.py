"""
B問題_0 or 1 Swap

1回の入れ替えで昇順にできるのは,入れ替え回数１回または0回（すでに昇順の時のみ）
"""

n = int(input())
p = list(map(int, input().split()))

diff_count = 0
for i, p_i in enumerate(p):
  if i + 1 != p_i: diff_count += 1
print("YES" if diff_count in (0, 2) else "NO")