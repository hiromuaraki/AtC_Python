"""
SNS クエリ (Hard)
(https://algo-method.com/tasks/871)

同じフォロワー集合を持つユーザーが何人いるか
frozenset = 変更できないset
"""

from collections import defaultdict

N,Q = map(int, input().split())
followers = [set() for _ in range(N)]

cnt = defaultdict(int)
empty = frozenset()
cnt[empty] = N

for _ in range(Q):
    line = list(map(int, input().split()))
    query = line[0]

    if query == 0:
        x, y = line[1], line[2]

        if x not in followers[y]:
            old = frozenset(followers[y])
            cnt[old] -= 1

            followers[y].add(x)

            new = frozenset(followers[y])
            cnt[new] += 1
    elif query == 1:
        x, y = line[1], line[2]

        if x in followers[y]:
            old = frozenset(followers[y])
            cnt[old] -= 1

            followers[y].remove(x)

            new = frozenset(followers[y])
            cnt[new] += 1
    else:
        z = line[1]
        key = frozenset(followers[z])
        print(cnt[key] - 1)


    