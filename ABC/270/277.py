"""
B問題_Playing Cards Validation
"""

n = int(input())
st = set()
t = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"}
s = [input() for _ in range(n)]
count = 0
for s_i in s:
  if s_i[0] not in ("H", "D", "C", "S"): break
  if s_i[1] not in t: break
  if s_i in st: break
  count += 1
  st.add(s_i)
print("Yes" if count == n else "No")
