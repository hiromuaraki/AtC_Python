s = list(input())
t = sorted(s)
c = t[-1] if t[0] == t[1] else t[0]
print(s.index(c) + 1)