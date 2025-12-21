"""
タスクの消化（貪欲法）・・・・解けない
"""

N = int(input())
tasks = [[] for _ in range(N)]

ans = 0
for i in range(N):
  A,B = map(int, input().split())
  tasks[A - 1].append(B)

cnt = [0]*101
ans = 0

for d in range(N):
  # d日目から実行可能なタスクをcntに追加する
  for b in tasks[d]:
    cnt[b] += 1

  for b in range(100, 0, -1):
    if cnt[b] > 0:
      ans += b
      cnt[b] -= 1
      break
  print(ans)

