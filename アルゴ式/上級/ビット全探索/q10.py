"""
パングラムを作る
(https://algo-method.com/tasks/1079ZGag)

ビット全探索＋部分集合の合成＋集合の管理
"""

n = int(input())
w = input().split()
ans = 10**9
for S in range(1 << n):
    chars = set()
    t = set()
    for i in range(n):
        if S & (1 << i):
            chars |= set(w[i]) # 文字集合
            t.add(w[i])

    if len(chars) == 26:
        ans = min(ans, len(t))
print(ans if ans != 10**9 else -1)



