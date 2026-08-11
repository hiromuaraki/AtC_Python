"""
挿入・削除・検索 (連想配列)
(https://algo-method.com/tasks/868)

"""

from collections import Counter

N = int(input())
A = input().split()
Q = int(input())

counter = Counter(A)

for _ in range(Q):
    query, s = input().split()
    query = int(query)

    if query == 0:
        counter[s] += 1
    elif query == 1:
        counter[s] = 0
    else:
        print(counter[s])