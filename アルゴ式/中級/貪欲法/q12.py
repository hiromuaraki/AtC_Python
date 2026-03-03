"""
区間スケジューリング問題
(https://algo-method.com/tasks/363)
"""

n = int(input())
st = [tuple(map(int, input().split())) for _ in range(n)]
# 予定の終了時刻が早い方から消化していくのが最適
st.sort(key=lambda x: x[1])

last_time = 0 # 前回の終了時刻を保持
count = 0
for s,t in st:
  if last_time <= s:
    last_time = t
    count += 1
print(count)



