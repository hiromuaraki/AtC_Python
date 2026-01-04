s = list(input())
t = list(input())

n = len(s)
for i in range(n):
  if s[i] != t[i]:
    t[i], t[i + 1] = t[i + 1], t[i]
    break

print("Yes" if s == t else "No")
