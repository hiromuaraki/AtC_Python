"""
トーナメント
(https://algo-method.com/tasks/617fPVr)
"""
from collections import defaultdict

N = int(input())
dict = defaultdict(int)
lst = []
for _ in range(N - 1):
    s, a, _, b, t = input().split()
    a, b = int(a), int(b)

    if a < b:
        dict[s] += 1
    else:
        dict[t] += 1

    if s not in lst:
        lst.append(s)
    if t not in lst:
        lst.append(t)

for s in lst:
    if s not in dict:
        print(s)

    

    

