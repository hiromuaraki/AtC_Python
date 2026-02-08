"""
ひもの本数
(http://algo-method.com/tasks/1679i9so)

区間[A, B]に入る要素数を数える問題
A以上になる最初の位置
B以下である最後の位置

2つ境界がある
右端 - 左端 + 1
"""
import bisect

n = int(input())
l = sorted(map(int, input().split()))
q = int(input())

for _ in range(q):
    a,b = map(int, input().split())
    left = bisect.bisect_left(l, a) # A以上が始まる位置
    right = bisect.bisect_right(l, b) # B以下が終わった「次」
    # A以上B以下の個数を数える
    print(max(0, right - left))

for _ in range(q):
    A, B = map(int, input().split())

    # A以上の最小index
    ok, ng = n, -1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if l[mid] >= A:
            ok = mid
        else:
            ng = mid
    left = ok

    # Bを超える最小index
    ok, ng = n, -1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if l[mid] > B:
            ok = mid
        else:
            ng = mid
    right = ok

    print(max(0, right - left))


  

  

  

