"""
挿入、削除、検索クエリ
(https://algo-method.com/tasks/1128iYHC)
"""

n,x = map(int, input().split())
q = int(input())

for _ in range(q):
    query_type, v = map(int, input().split())
    if query_type == 0:
        x |= 1 << v
        print(x, 1 << v)      
    elif query_type == 1:
        x &= ~(1 << v)
        print(x, ~(1 << v))
    else:
        print("Yes" if x >> v & 1 == 1 else "No")
        print(x, x >> v)