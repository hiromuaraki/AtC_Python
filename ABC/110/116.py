"""
B問題_Collatz Problem

重複した数が初めて出てくるのは何番目か？
"""

s = int(input())
st = set()
st.add(s)

while True:
  if s % 2 == 0: s //= 2
  else: s = 3*s + 1
  if s in st: break
  st.add(s)
print(len(st) + 1)
  

