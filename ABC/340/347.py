"""
Substring
"""
s = input()
n = len(s)
st = set()
for i in range(n):
  t = ""
  for j in range(i, n):
    t += s[j]
    st.add(t)
print(len(st))