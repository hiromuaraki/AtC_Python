"""
B問題_Caesar Cipher
"""

s = input()
t = input()
n = len(s)
lst = []
for i in range(n):
  k = (ord(t[i]) - ord(s[i])) % 26
  lst.append(k)

for i in range(n - 1):
  if lst[i] != lst[i + 1]:
    print("No")
    exit()
print("Yes")  
    
