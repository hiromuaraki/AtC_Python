import re
import sys
import heapq  # 最小値または最大値を取り出すデータ構造（常に先頭がmin,maxの性質を持つ）
from collections import deque  # 両橋のデータの追加や削除が高速で行えるデータ構造
from collections import Counter
from queue import Queue  # 先入れ先出し（FIFO）
from math import sqrt
from itertools import permutations


# 再帰の深さの上限を変更
sys.setrecursionlimit(10**9)




"""
A問題_429_Too Many Requests
"""

N, M = map(int, input().split())
for i in range(1, N + 1):
  if i <= M:
    print("OK")
  else:
    print("Too Many Requests")

"""
B問題_429_N - 1・・・解けた
難易度？？
"""

# 別解
N, M = map(int, input().split())
A = list(map(int, input().split()))
print("Yes" if sum(A) - M in A else "No")

total = sum(A)
for a in A:
  if total - a == M:
    print("Yes")
    exit()
print("No")

"""
問題C_429_Odd One Subsequence・・・解けない
難易度201
"""

from collections import Counter

N = int(input())
A = list(map(int, input().split()))
counter = Counter(A)

ans = 0 
for count in counter.values():
  # v個の中から同じ値を2個選ぶ組合せ数 * 異なる値を1個選ぶ選択肢の数
  # 値vを2つ選ぶ * 値v以外を1つ選ぶ
  ans += count * (count - 1) // 2 * (N - count)

print(ans)


"""
問題A_428_Grandma's Footsteps
シミュレーション（苦手）
"""

S,A,B,X = map(int, input().split())

ans = 0
for time in range(X):
  if time % (A + B) < A:
    ans += S
print(ans)


S, A, B, X = map(int, input().split())
time = 0
ans = 0

while time < X:
    move = min(A, X - time)
    ans += S * move
    time += move
    time += B

print(ans)



"""
問題B
"""

from collections import Counter

N,K = map(int, input().split())
S = input()
t = [S[i - 1 : i + K - 1] for i in range(1, N - K + 2)]
counter = Counter(t)
max_val = max(counter.values())

ans = []
for k, v in counter.items():
  if max_val == v:
    ans.append(k)
print(max_val)
print(*sorted(ans))



"""
問題A_427_ABC > AC
真ん中の文字を削除した残りの文字列を出力
中央のインデックス位置を求めその位置から前と後ろの文字列を連結
"""

S = input()
c = len(S)//2
print(S[:c] + S[c + 1:])

# ダメなコード
S = list(input())
c = S[len(S)//2]
idx = S.index(c)
ans = ""
for i in range(len(S)):
  if i != idx:
    ans += S[i]
print(ans)



"""
問題B_427_Sum of Digits Sequence・・・解けた
難易度？？
桁和＋シミュレーション＋状態管理
"""

N = int(input())

ans = []
total = "1"
for i in range(N):
    s = sum(map(int, total))
    ans.append(s)
    total += str(s)

print(ans[-1] if ans else 2)


"""
問題C_427_Bipartize

ビット全探索（白・黒色の塗り方を2^N通り試す）
"""

N,M = map(int, input().split())
G = [tuple(map(int, input().split())) for _ in range(M)]

# 白／黒の塗り方の割り当てを2^N通り試す
ans = M
for bit in range(1 << N):
  delete_count = 0
  for u, v in G:
    if (1 & (bit >> u)) == (1 & (bit >> v)):
      delete_count += 1
  ans = min(ans, delete_count)

print(ans)



"""
問題A_426_OSversion
"""

X,Y = input().split()
K = { "Ocelot": 0, "Serval": 1, "Lynx": 2}
print("Yes" if K[X] >= K[Y] else "No")


"""
問題B_426_The Odd One Out・・・解けた
頻度分布
"""

S = input()
counter = Counter(S)
print(sorted(counter.items(), key=lambda s: s[1])[0][0])


"""
C問題_426_Upgrade Required・・・解けない

データ構造の持ち方
各PCのバージョンの更新状態を管理
→今どこまでが更新対象になっているかを管理する変数rを定義
"""


N,Q = map(int, input().split())
cnt = [1] * (N + 1) # OSのバージョンは始めは全部1個

r = 1 # 今のバージョンの更新地点のindex
for _ in range(Q):
  x,y = map(int, input().split())
  ans = 0
  while r <= x:
    ans += cnt[r]
    cnt[r] = 0
    r += 1
  cnt[y] += ans
  print(ans)      

"""
問題A_425_Sigma Cubes
"""

N=int(input())
ans = 0
for i in range(1, N+1):
  ans += (-1)**i * (i**3)
print(ans)


"""
問題B_425_findPermutatons_順列全探索・・・自力AC
難易度82
難しい

順列全探索＝N!通り試す

入力：-1,1 ≦ N与えられる
1..NまでのPを並べ替えた数列とAが一致するかを判定する

A＝
・-1＝何でもいい
・-1以外＝固定
・Aの中で重複していたらその時点で条件は成立しない

P＝重複してはいけない かつ 1以外の位置は固定

方針：
Aの要素の中に-1以外の要素が重複しているかを調べる。重複していたらその時点でNo

"""

# 自力解法（順列なし）
N = int(input())
A = list(map(int, input().split()))
P = list(range(1, N + 1))
for a in A:
  if a != -1 and A.count(a) >= 2:
    print("No")
    exit()

i = 0
while -1 in A:
  if P[i] not in A:
    A[A.index(-1)] = P[i]
  i = (i + 1) % N

print("Yes")
print(*A)


N = int(input())
A = list(map(int, input().split()))
p = [0]*N
c = []

for i in range(N):
  if A[i] != -1:
    c.append(A[i])
    p[i] = A[i]

    if c.count(A[i]) >= 2:
      print("No")
      exit()

cnt = len(p) - p.count(0)
# 順列全探索
for pp in permutations(range(1, N+1)):
  ok = 0
  for i in range(N):
    if A[i] != 0 and pp[i] == p[i]:
      ok += 1
  
  if ok == cnt:
    print("Yes")
    print(*pp)
    exit()

print("No")

# 公式解法
for p in permutations(range(1, N+1)):
  ok = True
  for i in range(N):
    ok &= A[i] == -1 or p[i] == A[i]
  if ok:
    print("Yes")
    print(*p)
    exit()
else:
  print("No")


"""
C問題_425_Rotate_Sum Query・・・解けない
難易度315

先頭からある場所までの総和を求めておく
r - lでlからrまでの差をO(1)で計算

先頭の配列から数列を末尾へX回移動する
開始位置を保持しておき、開始位置がN回回ったら元に戻る

(Si + X) % N → 移動の開始位置
累積和：N+1個の配列を準備し先頭からある場所までの総和事前に計算しておく
"""

N,Q = map(int, input().split())
A = list(map(int, input().split()))

S = [0] * (N+1)
for i in range(N):
  S[i + 1] = S[i] + A[i]

si = 0
for _ in range(Q):
  query = list(map(int, input().split()))
  t = query[0]
  if t == 1:
    c = query[1]
    si = (si + c) % N

  else:
    l, r = query[1:]
    l -= 1; r -= 1
    l = (l + si) % N
    r = (r + si) % N
    ans = 0
    if l <= r:
      ans = S[r + 1] - S[l]
    else:
      ans = S[N] - (S[l] - S[r + 1])
    print(ans)

"""
問題A_424_Isosceles
二等辺三角形かどうかを判定
二辺が等しいかどうかの場合分け
"""

A, B, C = map(int, input().split())
print("Yes" if A == B or B == C or C == A else "No")


"""
問題B_424_Perfect・・・解けた
難易度

全完した人を全員出力

頻度分布を取る
Mと等しいキーの値を出力
"""

N, M, K = map(int, input().split())
H = {}
for i in range(K):
    A, B = map(int, input().split())
    if A not in H:
        H[A] = 0
    H[A] += 1

    if H[A] == M:
        print(A, end=" ")


"""
問題C_424_New Skill Acquired ・・・解けない
有向グラフ＋BFS

難易度220？
計算量：O(N)



キューの準備:探索を開始するノードをキューに入れます。﻿
ノードの取り出し:キューからノードを一つ取り出します。﻿
隣接ノードの探索:取り出したノードから直接行ける（隣接する）未探索のノードを見つけます。﻿
キューへの追加:見つかった未探索のノードに訪問済みの印をつけ、キューに追加します。﻿
"""

# 公式解法
N = int(input())
graph = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    A, B = map(int, input().split())
    graph[A].append(i)
    graph[B].append(i)

visited = [0] * (N + 1)
visited[0] = 1


def dfs(v):
    visited[v] = 1
    for u in graph[v]:
        if not visited[u]:
            dfs(u)


dfs(0)
print(sum(visited) - 1)

# 別解
N = int(input())
G = [[] for _ in range(N)]
visited_ = [False] * N
que = deque()

for i in range(N):
    A, B = map(int, input().split())
    if A == 0:
        # スキル習得済みに変更
        visited_[i] = True
        que.append(i)
    else:
        A -= 1
        B -= 1
        G[A].append(i)
        G[B].append(i)

# BFS
while que:
    # 頂点を取り出す
    v = que.popleft()
    for i in G[v]:
        if not visited_[i]:
            que.append(i)
            visited_[i] = True

print(visited_.count(True))


"""
問題A_423_ScrayFee・・・解けない（算数）
難易度


1000円あたりC円の手数料が加算

最大でいくら引き出せるか
残高//（1000円＋手数料）*1000（整数除算：小数点以下切り捨て）
"""

X, C = map(int, input().split())
print(X // (1000 + C) * 1000)

# 別解（シミュレーション）
ans = 0
while True:
    now = ans + 1000
    if now + (now // 1000 * C) > X:
        break
    ans = now
print(ans)


"""
B問題_423_Locked Rooms・・・解けた
難易度？？
"""

N = int(input())
L = list(map(int, input().split()))

l, r = N, 0
for i in range(N):
  if L[i] == 0: continue
  r = max(r, i)
  l = min(l, i)

# 全て部屋が空いている場合
if l == N:
  print(0)
else:
  print(r - l)


# 修正前（自分の実装）
l, r = 0, 0
for i in range(N):
    if L[i] == 1:
        l = i
        break
for i in range(N - 1, -1, -1):  # 終了は0を含める
    if L[i] == 1:
        r = i
        break
print(r - l)


"""
C問題423_Lock All Doors・・・解けない
難易度？？
"""


N,R = map(int, input().split())
L = list(map(int, input().split()))

# 現在の開始位置から走査
def func(lst):
  cur, count = 0, 0
  for is_open in lst:
    if is_open == 1:
      # 開閉
      cur += 2
      continue
    # 閉
    count += 1 + cur
    cur = 0
  return count

ans = 0
ans += func(L[:R][::-1])
ans += func(L[R : N])
print(ans)


"""
問題A_422_Stage Clear（場合分けの問題）
"""

i, j = map(int, input().split("-"))
if j < 8:
    j += 1
elif i < 8 and j == 8:
    i, j = i + 1, 1

print(i, j, sep="-")

i, j = map(int, input().split("-"))
if j < 8:
    j += 1
elif i < 8 and j == 8:
    i += 1
    j = 1
print(i, j, sep="-")


"""
問題B_422_Looped Rope・・・自力AC・グリッド問題
難易度77

全て#の隣接する#の数が2件または4件ならYes,そうでなければNo

場合分けをなくす為上下左右のベクトル座標を用意
(行、列)＝(i, j)
上：(-1, 0)
下：(1, 0)
右：(0, 1)
左：(0, -1)
"""

H, W = map(int, input().split())
S = [input() for _ in range(H)]
# 上下左右の座標を準備
si = [-1, 1, 0, 0]
sj = [0, 0, -1, 1]

for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            continue
        count = 0
        # 上下左右の黒マスを確認
        for dy, dx in zip(si, sj):
            y, x = i + dy, j + dx
            # 移動マスの存在チェック
            if y < 0 or H <= y or x < 0 or W <= x:
                continue
            if S[y][x] == "#":
                count += 1
        if count not in (2, 4):
            print("No")
            exit()
print("Yes")

# 自力AC
H,W = map(int, input().split())
S = [input() for _ in range(H)]
D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(H):
  for j in range(W):
    count = 0
    if S[i][j] == "#":
      for dy, dx in D:
        y, x = dy + i, dx + j
        if not (0 <= y < H and 0 <= x < W):
          continue
        if S[y][x] == "#":
          count += 1
      if count not in (2, 4):
        print("No")
        exit()
print("Yes")


"""
C問題_422_AtCoder AAC Contest ・・・解けない
難易度？？
二分探索
単調性＝ある地点まではOK,ある地点からはNGの境界が切り替わるような性質
"""

T = int(input())

# 計算
for _ in range(T):
  a,b,c = map(int, input().split())
  print(min(a, c, (a + b + c) // 3))

# 二分探索
for _ in range(T):
  a,b,c = map(int, input().split())

  def f_calc(x):
    if x > min(a, c):
      return False
    return (a - x) + (c - x) + b >= x
  
  ok, ng = 0, a + b + c
  while (ng - ok > 1):
    mid = (ok + ng) // 2
    if f_calc(mid):
      ok = mid
    else:
      ng = mid
  print(ok)



"""
問題A_421_Misdelivery
"""

N = int(input())
S = [input() for _ in range(N)]
X, Y = list(input().split())
X = int(X)
print("Yes" if S[X - 1] == Y else "No")

"""
問題B_421_Fibonacci Reversed・・・解けた
難易度55
"""

A = list(input().split())
fibn = [0] * 10
fibn[0], fibn[1] = A[0], A[1]

for i in range(2, 10):
    n = str(int(fibn[i - 2]) + int(fibn[i - 1]))
    fibn[i] = int(n[::-1])
print(fibn[-1])


"""
問題C_421_Alternated
"""

N = int(input())
S = input()
A = [0] * (2 * N)

for i in range(len(S)):
    if i % 2 != 0 and S[i] != "B":
        A[i] = 1
    elif i % 2 == 0 and S[i] != "A":
        A[i] = 1

cnt = 0
for i in range(len(A) - 1):
    if sum(A[i:3]) == 2:
        cnt += 1
print(cnt)


"""
問題A_
"""


"""
問題B_420_Mostjudfe the game・・・解けない
難易度74
"""

n, m = map(int, input().split())
s = [input() for _ in range(n)]
ans = [0] * n
for i in range(m):
    c0 = []
    c1 = []
    for j in range(n):
        if s[j][i] == "1":
            c1.append(j)
        else:
            c0.append(j)
    if len(c0) > len(c1):
        for k in c1:
            ans[k] += 1
    else:
        for k in c0:
            ans[k] += 1

ma = max(ans)
for i in range(n):
    if ans[i] == ma:
        print(i + 1, end=" ")


"""
問題A_419_AtCoder Language
"""

S = input()
k = {"red": "SSS", "blue": "FFF", "green": "MMM"}
print(k[S] if S in ("red", "blue", "green") else "Unknown")


"""
問題B_419_GetMin・・・解けた
heapのデータ構造の理解必須
先頭に常に最小または最大の要素を保持できるに二分木構造
"""

Q = int(input())
a = []
a.pop()
# 非効率のアルゴリズム min * remove
for _ in range(Q):
    query = input().split()
    q_type = int(query[0])
    if q_type == 1:
        a.append(int(query[1]))
    else:
        min_val = min(a)
        print(min_val)
        a.remove(min_val)


# heap版アルゴリズム 高速
heap = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        heapq.heappush(heap, query[1])  # 要素をheapへ追加
    else:
        print(heapq.heappop(heap))  # heapから最小値を取り出す（pop）と同じ動き


"""
問題A_418_I'm a teapot
"""

N = int(input())
S = input()
print("Yes" if S[-3:] == "tea" else "No")

"""
問題B_418_You're a teapot

＊問題文の数式や定義を正確に噛み砕く力が弱い

先頭と末尾が't'
|t| >= 3

r+2 →部分文字列の長さを3以上で開始するため
長さ＝l - r + 1
中間の長さ＝l - r - 1（両端（先頭と末尾）を除いた中間の長さ）
"""

# 修正前
# for r in range(N):
#     if S[r] != 't': continue
#     for l in range(r+1, N):
#         if S[r] != 't' or S[l] != 't':
#             continue
#         n = l - r - 1
#         if n >= 2:
#           ans = max(ans, (S[r+1:l].count('t'))/n)
# print(ans)


# 修正後（正解）
S = input()
N = len(S)
ans = 0
for r in range(N):
    if S[r] != "t":
        continue
    for l in range(r + 2, N):
        if S[l] != "t":
            continue
        length = l - r + 1
        x = S[r : l + 1].count("t")
        ans = max(ans, (x - 2) / (length - 2))
print(ans)


"""
問題A_417_ASubstring
"""

N, A, B = map(int, input().split())
S = input()
print(S[A : N - B])


"""
問題B_417_Search and Delete
"""

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for b in B:
    if b in A:
        A.remove(b)
print(*A)

"""
問題A_416_Vacation Validation
"""

N, L, R = map(int, input().split())
S = input()
print("Yes" if "x" not in S[L - 1 : R] else "No")

"""
問題B_416_1D Akari
"""

# 自分で考えたロジック
# リストはいらない
S = input()
t = ""
section = True

for s in S:
    if s == "#":
        t += "#"
        section = True
    elif s == "." and section:
        t += "o"
        section = False
    else:
        t += "."
print(t)

S = input()

T = []
section = False
for c in S:
    if c == "#":
        T.append("#")
        section = False
    elif c == "." and not section:
        T.append("o")
        section = True
    else:
        T.append(".")
print("".join(T))

"""
問題A_415_Unsupported Type
"""

N = int(input())
A = list(map(int, input().split()))
X = int(input())
print("Yes" if X in A else "No")

"""
問題B_415_Pick Two・・・解けた

O(N）で出力できる
"""

S = input()
ans = []
for i in range(len(S)):
    if S[i] == "#":
        ans.append(i + 1)

    if len(ans) == 2:
        print(f"{ans[0]},{ans[1]}")
        ans = []


"""
問題A_414：Streamer Takahashi
"""

N, L, R = map(int, input().split())
ans = 0
for i in range(N):
    X, Y = map(int, input().split())
    if X <= L and R <= Y:
        ans += 1
print(ans)

"""
問題B_414：String Too Long・・・解けない（メモリエラー）・・・自力AC
難易度？？
"""
N = int(input())
MAX_LENGTH = 10**6
s = ""
for _ in range(N):
    C, L = input().split()
    L = int(L)
    if L > MAX_LENGTH:
        print("Too Long")
        exit()

    if len(s) > 100:
        print("Too Long")
        exit()
    s += C * L

print(s if s != "" and len(s) <= 100 else "Too Long")


"""

"""

"""
問題A_413：Content Too Large
"""

N, M = map(int, input().split())
A = list(map(int, input().split()))
print("Yes" if sum(A) <= M else "No")


"""
問題B_413：cat2・・・解けた（組合せ全探索）
問題文を正確に理解する必要あり
i ≠ j の場合のみSi+Sjの文字列を連結したものをsetに入れていく
データ構造をセットにする事により重複を除いて管理できる。
"""

N = int(input())
S = [input() for _ in range(N)]
C = set()
for s in S:
    for t in S:
        if s != t:
            C.add(s + t)
print(len(C))


"""
問題A_412：Task Failed Successfully 
"""

N = int(input())
ans = 0
for i in range(N):
    A, B = map(int, input().split())
    if A < B:
        ans += 1
print(ans)


"""
問題B_412：Precondition・・・解けなかった

先頭ではない英大文字の直前の文字がTに含まれているか
先頭ではない＝0番目ではない英大文字
"""


S = input()
T = input()
ans = "Yes"
for i in range(1, len(S)):
    if S[i].isupper() and S[i - 1] not in T:
        ans = "No"
        break
print(ans)

"""
問題A_411：Required Length
"""

P = input()
L = int(input())
print("Yes" if len(P) >= L else "No")


"""
問題B_411：Distance Table・・・解けた
時間計算量：O(N^2)
総和を駅iごとに出力する
"""

# 自分の解法
N = int(input())
D = list(map(int, input().split()))
L = [[] for _ in range(N)]
for i in range(N - 1):
    ans = 0
    for j in range(N - 1 - i):
        ans += D[i + j]
        L[i].append(ans)
    print(*L[i])

# シンプルなアルゴリズム(inadaiさん)
for i in range(N - 1):  # 4回
    ans_1 = []
    for j in range(i + 1, N):  # 3回
        ans_1.append(sum(L[i:j]))
    print(*ans)


"""
C問題_411：Black Intervals（解説見ながら土日やる）・・・解けない
"""

# usmstkさんの解法（ビット演算を0,1で色の反転を実現）
N, Q = map(int, input().split())
A = list(map(int, input().split()))

color = [0] * (N + 2)
ans = 0

for i in A:
    if color[i - 1] == color[i] and color[i] == color[i + 1]:
        ans += 1
    elif color[i - 1] != color[i] and color[i] != color[i + 1]:
        ans -= 1

    # ここの結果は0,1しか入らない
    color[i] ^= 1  # ビット演算（a,bのうち一方だけが1であれば1,そうでなければ0）
    print(ans)


"""'
問題A_410：G1
"""

N = int(input())
A = list(map(int, input().split()))
K = int(input())
ans = 0
for a in A:
    if K <= a:
        ans += 1
print(ans)

"""'
問題B_410：Reverse Proxy・・・解けた

時間計算量：O(N^3）
"""

N, Q = map(int, input().split())
X = list(map(int, input().split()))
BOX = [0] * N
ans_1 = []
for x in X:
    if x == 0:
        x = BOX.index(min(BOX)) + 1
    BOX[x - 1] += 1
    ans_1.append(x)
print(*ans_1)

"""
問題C_410：Rotatable Array・・・解けない（シフト）

時間計算量の問題

Aの要素とは別に現在のポジションを表す
offsetを持っておく

(offset + 要素) % Nとし計算量を
O(N + Q)に改善する
"""

N, Q = map(int, input().split())
A = list(range(1, N + 1))
pos = 0
for i in range(Q):
    T = list(map(int, input().split()))
    type = T[0]
    if type == 1:
        A[(T[1] - 1 + pos) % N] = T[2]
    if type == 2:
        print(A[(T[1] - 1 + pos) % N])
    if type == 3:
        pos = (pos + T[1]) % N


"""
問題A_409：Conflict
"""

n = int(input())
t = list(input())
a = list(input())
for i in range(n):
    if t[i] == a[i] == "o":
        print("Yes")
        exit()
print("No")


"""
問題B_409：Citation・・・解けない
時間計算量：O(N^2)

x以上の要素が重複を含めてx回以上現れる。
x = 1..Nまでの値
a >= x回以上現れる回数を求める

1..N回の中で各要素の件数をカウントしX以上の時、条件が成立する
"""

# 要修正
N = int(input())
A = list(map(int, input().split()))
ans = 0

for x in range(N, -1, -1):
    cnt = 0
    for a in A:
        if a >= x:  # 要素aの登場回数を求める
            cnt += 1
    if cnt >= x:  # 1..Nまでの間に登場した回数がX以上の場合のみ条件を満たす
        print(x)
        break


"""
問題A_408：TimeOut（経過時間シミュレーション）
90%
連続して長老が起きているかを判定する

起きているかの判定は前回叩かれてからs + 0.5以下かどうか
"""
N, S = map(int, input().split())
T = list(map(int, input().split()))
time = 0
for i in range(N):
    if S + 0.5 <= T[i] - time:
        print("No")
        exit()
    time = T[i]
print("Yes")

"""
問題B_408：Compression・・・解けた
100%
重複を除いて小さい順に出力
"""

n = int(input())
m = set(map(int, input().split()))
print(sorted(m))

"""
C問題_408：Not All Covered・・・解けない（後から復習）

最小で何個の砲台を壊せば城壁が守られていない状態になるか
"""

n, m = map(int, input().split())
imos = [0] * n + 1

for i in range(m):
    l, r = map(int, input().split())
    # 区間の開始地点+1と終了地点-1をimosへ登録
    l -= 1
    imos[l] += 1
    imos[r] -= 1

print(imos)

"""
問題A_407：Approximation
100%
A/Bの差が最小となる値を出力
"""

a, b = map(int, input().split())
print(round(a / b))

"""
B問題_407：P(X or Y)・・・解けない（勉強が必要）
70%
確率を求める
2つの出目の合計がx以上
2つの出目の差の絶対値がy以上である

x = 出目の合計
y = 出目の差

|a  - b| >= y
言い換えると
b - a >= y
a + y >= b

bがyよりa以上大きいかを判定

重複を除いたセットを作成しその要素数で割る

なぜ解けないのか
＊2つの出目の差の絶対値がy以上を理解できていない
"""
# OK
X, Y = map(int, input().split())
cnt = 0
for a in range(1, 7):
    for b in range(1, 7):
        if a + b >= X or abs(a - b >= Y):
            cnt += 1
print(cnt / 36)

# x, y = map(int, input().split())
# count = 0
# for a in range(1, 7):
#   for b in range(1, 7):
#     if x <= a + b or a + y <= b or b + y <= a:
#       count += 1
# print(count / 36)

"""
問題C_407：Security 2・・・解けない（後から復習）
"""

"""
問題A_406：Not Acceptable
"""

a, b, c, d = map(int, input().split())
print("Yes" if (c, d) < (a, b) else "No")

"""
問題B_406：Product Calculator・・・解けた
"""

n, k = map(int, input().split())
numbers = list(map(int, input().split()))
res = 1
for num in numbers:
    res *= num
    if k + 1 <= len(res):
        res = 1
print(res)

"""
問題A_405：Is it rated?
"""

r, x = map(int, input().split())
ans = "No"
if x == 1 and 1600 <= r <= 2999:
    ans = "Yes"
if x == 2 and 1200 <= r <= 2399:
    ans = "Yes"
print(ans)

"""
問題B_405：Not All・・・解けた

1以上M以下の整数が含まれている最小の回数を求める

すべて含まれている時のみ最小件数をカウントし要素を削除する
"""

n, m = map(int, input().split())
nn = list(map(int, input().split()))
a = [i for i in range(1, m + 1)]
count = 0
for _ in range(n):
    if all(data in nn for data in a):
        nn.pop()
        count += 1
    else:
        break
print(count)

"""
C問題_405：Sum of Product・・・解けない（復習）
時間計算量：O(N)
"""


"""
問題A_404：Not Found
"""

s = set(input())
c = set(chr(ord("a") + i) for i in range(26))
print(list(c - s)[0])


"""
問題B_404：Grid Rotation・・・解けない（復習）

グリッドSとTを一致させる最小回数を求める
グリッドSの回転操作＋色の塗り替え回数 = 最初回数

間違ったプログラム（これをベースに後で修正）
グリッドをSを90度4回回転する（0, 1, 2, 3）
1周しても元の位置に戻る
(i, j) = (j, N - i - 1)

方針：

"""

N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]
cur, ans = S, 1e9


# グリッドの回転
def rotate(S: list, N: int) -> list:
    res = [["." for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            res[j][N - 1 - i] = S[i][j]
    return res


# 色の違う場所をカウントする
def count_diff(S: list, T: list) -> int:
    cnt = 0
    for i in range(N):
        for j in range(N):
            if S[i][j] != T[i][j]:
                cnt += 1
    return cnt


# メイン処理
for row_count in range(N):
    ans = min(ans, count_diff(cur, T) + row_count)
    cur = rotate(cur, N)
print(ans)


"""
問題A_403：Odd Position Sum
"""
n = int(input())
num = list(map(int, input().split()))
print(sum(num[i] for i in range(n) if i % 2 == 0))

"""
問題B_403：Four Hidden・・・解けない
時間計算量：O(N^2)またはO(N^4)
方針：
2重ループで全探索する
? = なんでも入っていい
?以外は一致していないといけない

T - U + 1通りの回数をループする
tが？でないかつtとuの文字列が一致しなければ連続文字列ではないと判定する

別解
4重のループで全探索
あらかじめtの文字列より？の位置のindexをリストで作成し、
？にアルファベットを26^4通り分当てはめ一致するまで繰り返す
26^4 = 456_976回
"""
# 解答
T = input()
U = input()
for i in range(len(T) - len(U) + 1):
    OK = True
    for j in range(len(U)):
        if T[i + j] != "?" and T[i + j] != U[j]:
            OK = False
            break
    if OK:
        print("Yes")
        exit()
print("No")


"""
問題A_402：CBC
"""
# 別解
s = input()
print(*re.findall("A-Z", s), end="")

ans = [c for c in s if c.isupper()]
print(*ans)

"""
問題B_402：Restaurant Queue・・・解けた
"""
q = int(input())
queue = []
for i in range(q):
    type = list(map(int, input().split()))
    if type[0] == 1:
        queue.append(type[1])
    else:
        print(queue[0])
        queue.pop(0)

"""
問題A_401：Status Code
"""

code = int(input())
print("Success" if 200 <= code <= 299 else "Failure")

"""
問題B_401：Unauthorized・・・解けた

ログアウト状態で非公開ページアクセスした回数＝認証エラー回数
"""

n = int(input())
user = [input() for _ in range(n)]
res = ""
cnt = 0
for current_user in user:
    if current_user == "login":
        res = "login"
    if current_user == "private" and res != "login":
        cnt += 1
    if current_user == "logout":
        res = "logout"


"""
問題A_400：ABC400 Party
"""

a = int(input())
print(400 // a if 400 % a == 0 else -1)

"""
問題B_400：Sum of Geometric Series・・・解けた
"""

n, m = map(int, input().split())
ans = 1
for i in range(1, m + 1):
    ans += n**i
print(ans if ans <= 1e9 else "inf")

"""
問題A_399：Hamming Distance
"""

n = int(input())
s = input()
t = input()
cnt = 0
if s != t:
    print(sum(1 for i in range(n) if s[i] != t[i]))
else:
    print(cnt)

"""
問題B_399：Ranking with Ties・・・解けない

時間計算量：O(N^2)

＊自分より得点の高い人数を数える

複雑な問題は言い換えができないか考える
プログラムはシンプルに考える
"""
N = int(input())
P = list(map(int, input().split()))
for i in range(N):
    rank = 1
    for j in range(N):
        if P[i] < P[j]:
            rank += 1
    print(rank)

"""
問題A_398：Doors in the Center
"""

n = int(input())
ans = ["-"] * n
mid = n // 2

if n % 2 == 0:
    ans[mid - 1 : mid + 1] = "=="
else:
    ans[mid] = "="
print("".join(ans))

"""
問題B_398：Full House 3・・・解けた（安定して解けない）

時間計算量：O(N^2)
同じxが書かれたカード3枚+同じyが書かれたカード2枚
=フルハウス

セットで重複を除いたデータにしセットの件数分、
元データから重複データの件数を検索し、重複リストへ追加
リストの件数は1件の場合は、その時点でNo
ソートで降順に並べ替えをし、0番目と1番目が3件以上かつ2件以上の時だけYes, それ以外はNo
"""

A = list(map(int, input().split()))
C = set(A)
ans = "No"
dup = [A.count(a) for a in C]
dup.sort(reverse=True)
# 配列の参照外にアクセスしない為の条件
if len(dup) == 1:
    print(ans)
    exit()
elif dup[0] >= 3 and dup[1] >= 2:
    ans = "Yes"
print(ans)

"""
問題A_397：Thermometer
"""
x = int(input())
ans = 0
if x >= 38:
    ans = 1
elif 37.5 <= x < 38.0:
    ans = 2
else:
    ans = 3
print(ans)

"""
問題B_397；Ticket Gate Log・・・解けない（70%は解けた）

i,oのみからなる文字列Sが与えられる

方針
i なら 'o', oなら'i'

iなら'o',oなら'i'に切り替える処理を文字列長分
繰り返し文字連結した新しい文字列を作成する

末尾が'i'なら1を足す
"""

S = input()
cnt, T = 0, "i"
for log in S:
    if log == T:
        T = "o" if T == "i" else "i"
    else:
        cnt += 1
if S[-1] == "i":
    cnt += 1
print(cnt)

"""
問題A_396：Triple Four
"""

n = int(input())
a = list(map(int, input().split()))
for i in range(n - 1):
    if a[i] == a[i + 1] == a[i + 2]:
        print("Yes")
        exit()
print("No")

"""
問題B_396：Card Pile・・・解けた
末尾に追加し末尾を削除
"""
cards = [0] * 100
q = int(input())
for i in range(q):
    type = input().split()
    if type[0] == "1":
        cards.append(type[1])
    if type[0] == "2":
        print(cards.pop())

"""
問題A_395：Strictly Increasing? 
"""

n = int(input())
num = list(map(int, input().split()))
for i in range(n):
    if num[i + 1] < num[i]:
        print("No")
        exit()
print("Yes")

"""
問題B_395：Make Target・・・解けた
時間計算量：O(N^3)

方針
N**2のグリッド
j = N - 1 - i
行が列を超えていなければ色の塗り替え処理をする
iが偶数ならば黒
iが奇数なら白と黒白交互に塗り替えていく
"""
N = int(input())
S = [["."] * N for _ in range(N)]

for i in range(N):
    j = N - 1 - i
    if i <= j:
        for x in range(i, j + 1):
            for y in range(i, j + 1):
                if i % 2 == 0:
                    S[x][y] = "#"
                else:
                    S[x][y] = "."
for row in S:
    print("".join(row))

"""
問題A_394：22222
"""
c = list(input()).count("2")
print("2" * c)

"""
問題B_394：cat・・・解けた

＊配列の容量が足りない場合は実行時エラーとなるケースがある
問題文をよく読む

文字列の長さの昇順に並べ替える
"""

n = int(input())
ans = [""] * n * 50
s = [input() for _ in range(n)]
for i in range(n):
    ans[len(s[i])] = s[i]
print(*ans, sep="")

"""
問題C_394：Debug（土日復習する）
"""
# これだとTLE
# while 'WA' in s:
#   s = s.replace('WA', 'AC',1)
# print(s)

s = list(input())
for i in range(len(s) - 2, -1, -1):
    if s[i] == "W" and s[i + 1] == "A":
        s[i] = "A"
        s[i + 1] = "C"
print("".join(s))


"""
問題A_393：Poisonous Oyster

高橋くん1, 2
青木くん1, 3

sick fine
 高橋くんがお腹を壊した= 2

sick sick
 両方ともお腹を壊す=1

fine sick
 青木くんがお腹を壊した= 3
fine fine = 4
 両方とも元気

"""

t, a = input().split()
ans = 0
if t == a == "sick":
    ans = 1
if t == a == "fine":
    ans = 4
if t == "sick" and a == "fine":
    ans = 2
if t == "fine" and a == "sick":
    ans = 3
print(ans)

"""
問題B_393：A..B..C・・・解けた

時間計算量：O(N^3) = 10^6

方針：
以下の条件が成立しない時だけ文字列が'ABC'に連続する場合と判断
j - i = k - jの時の文字列が等間隔と判断しカウント件数を加算する
i >= j または j >= k
i ≠ A かつ j ≠ B かつ k ≠ c場合はスキップする
j - i == k - jが成立したら件数をカウントする
"""
s = input()
cnt = 0
n = len(s)
for i in range(n):
    if s[i] == "A":
        for j in range(n):
            if s[j] == "B":
                for k in range(n):
                    if i >= j or j >= k:
                        continue
                    if s[k] == "C" and j - i == k - j:
                        cnt += 1
print(cnt)

"""
問題A_392：Shuffled Equation

昇順に並べ替えてa1 * a2 == a3のみ比較する
"""
a = list(map(int, input().split()))
ans = "No"
a.sort()
if a[0] * a[1] == a[2]:
    ans = "Yes"
print(ans)

"""
問題B_392：Who is Missing?・・・解けた

時間計算量：O(N)
整数numbersに含まれない値をn以上になるまで追加していく
"""

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
ans = [i for i in range(1, n + 1) if num not in numbers]
print(n - m)
print(*ans)

"""
問題C_392：Bib（後でやる）
"""

"""
問題A_391：Lucky Direction
方角
"""

d = input()
ans = ""
for s in d:
    if s == "N":
        ans += "S"
    if s == "E":
        ans += "W"
    if s == "S":
        ans += "N"
    if s == "W":
        ans += "E"
print(ans)

"""
問題B_391：Seek Grid・・・解けない

時間計算量：O(N^4)

Sのグリッドの中にTグリッドと一致する(a, b)座標を求める
(a, b)は左上のマス
N - M + 1通の中の条件が成立するa,bの座標を探す為の全探索
i, jはSの中からTのグリッドと一致している座標を探す為の全探索

全探索しSとTが一致していなければフラグを変える
i,jの全探索終了時点でフラグがTrueのa,bが一致しているため
条件を満たす座標となる。

最後の+1は配列の0から開始しているのを問題に合わせて+1に戻している
"""

N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(M)]
# a,bをN-M+1の範囲で全探索
for a in range(N - M + 1):
    for b in range(N - M + 1):
        ok = True  # a,bの座標が条件を満たすかを判断
        # i,jを1..Mの範囲で全探索
        for i in range(M):
            for j in range(M):
                if S[a + i][b + j] != T[i][j]:
                    ok = False
        if ok:
            print(a + 1, b + 1)

"""
C問題_391：Pigeonhole Query・・・解けない（土日に復習）

1 P H : 鳩P を巣H に移動させる。
2 : 複数の鳩がいる巣の個数を出力する。

差分に注目して更新する
"""

n, q = map(int, input().split())
h = [1] * n

for i in range(q):
    type = list(map(int, input().split()))
    if type[0] == 1:
        pass
    else:
        print(0)

"""
問題A_390：12435
"""

num = list(map(int, input().split()))
target = [i for i in range(1, 6)]
ok = False
for i in range(len(num) - 1):
    if num[i + 1] < num[i]:
        num[i + 1], num[i] = num[i], num[i + 1]
        ok = True
        break
print("Yes" if ok and "".join(str(num)) == str(target) else "No")


"""
問題B_390：Geometric Sequence・・・解けた

等比数列

後ろの数 ÷ 前の数 = 比
Ai, Ai + 1,Ai + 2,Ai + 3,Ai + 4..Ai + N

整数で等比を比較したい
→Ai+1/Ai = Ai+2/Ai+1 = Ai+1 * Ai+1 = Ai*Ai+2
"""
n = int(input())
a = list(map(int, input().split()))
for i in range(n - 2):
    if a[i + 1] ** 2 != a[i] * a[i + 2]:
        print("No")
        exit()
print("Yes")

"""
問題A_389：9*9
"""
s = input()
print(int(s[0]) * int(s[2]))

"""
問題B_389：tcaF・・・解けた
時間計算量：O(N)

N! = Xを求める
N!= N * (N-1) * (N-2) * ...3 * 2 * 1
N * N+1 * N+2 * N+3 *...
"""

n = int(input())
x = 1
for i in range(2, n + 1):
    x *= i
    if n == x:
        break
print(i)

"""
問題A_388：?UPC
"""
print(input()[0] + "UPC")

"""
問題B_388：Heavy Snake・・・解けた

N=蛇の数
D=行数
蛇の重さ＝Ti（太さ） * Li（長さ）

すべての長さがk伸びた時の最も重い蛇の重さ
"""

n, d = map(int, input().split())
hv = [list(map(int, input().split())) for _ in range(n)]
k = 0
while k < d:
    k = k + 1
    max_value = 0
    for tl, li in hv:
        weight = tl * (li + c)
        max_value = max(max_value, weight)
    print(max_value)

"""
問題A_387：Happy New Year 2025
"""
a, b = map(int, input().split())
print((a + b) ** 2)

"""
問題B_387：9x9 Sum・・・解けた
時間計算量：O(N^2)
xではないものの総和を出力

99の性質
45^2 = 2025


＊違う段の値も対象になる
"""

x = int(input())
total = 0
for i in range(1, 10):
    for j in range(1, 10):
        if i * j != x:
            total += i * j
print(total)

"""
問題A_386：Full House 2
xが3枚, yが2枚でフルハウス
４枚の手札

4枚のカード
+1枚カードが来た時にフルハウスか判定

13^5

2 + 2 = フルハウス
3 + 1 = フルハウス
(1 ,3) = 5
  (2, 2) = 5
    (3, 1) = 5

フルハウスの時だけ必ず2組のペアになる
カウント件数を追加し、サイズが2件の時のみフルハウスと判定
"""

# 修正後
Card = list(map(int, input().split()))
C = set(Card)
ans = [Card.count(a) for a in C]
if len(ans) == 2:
    print("Yes")
else:
    print("No")

# card = list(map(int, input().split()))
# c = set(card)
# ans = [card.count(x) for x in c]
# ans.sort(reverse=True)
# if ans[0] == 3 and ans[1] == 1:
#   print('Yes')
#   exit()
# if ans[0] == 2 and ans[1] == 2:
#   print('Yes')
#   exit()
# print('No')

"""
問題B_386：Calculator・・・解けない

0と0以外
0が連続しているかいないか

シンプルに考える

'00'を1としてカウントしたい

方針
'00'をすべて'x'に変換し1文字にし文字列の長さを出力する
"""

print(len(input().replace("00", "X")))

"""
問題A_385：Equally
"""

a, b, c = map(int, input().split())
ans = "No"
if a == b == c:
    ans = "Yes"
if a + b == c or a + c == b or b + c == a:
    ans = "Yes"
print("No")

"""
問題B_385：Santa Claus 1（グリッド）・・・解けた

時間計算量：O(N)

#・・・通行不可能
.・・・通行可能であり家が建っていない
@・・・通行可能であり家が建っている

サンタクロースがはじめ(x, y)の座標にいる

  Tiが U かつマス (x−1,y) が通行可能ならマス(x−1,y) に移動する。
  Tiが D かつマス (x+1,y) が通行可能ならマス (x+1,y) に移動する。
  Tiが L かつマス (x,y−1) が通行可能ならマス (x,y−1) に移動する。
  Tiが R かつマス (x,y+1) が通行可能ならマス (x,y+1) に移動する。
  それ以外の場合、マス (x,y) に留まる。


通過したマス(x, y)の情報を保持する


"""

# 修正前
# def is_pass(s: list, x: int, y: int) -> bool:
#   if s[x][y] == '.' or s[x][y] == '@': return True
#   return False

# h,w,x,y = map(int, input().split())
# s = [list(input()) for _ in range(h)]
# t = input()
# sc = set(); h_cnt = 0
# x -= 1; y -= 1
# for move in t:
#   if move == 'L' and is_pass(s, x, y - 1):y -= 1
#   if move == 'R' and is_pass(s, x, y + 1):y += 1
#   if move == 'U' and is_pass(s, x - 1, y):x -= 1
#   if move == 'D' and is_pass(s, x + 1, y):x += 1

#   if s[x][y] == '@':
#     if (x + 1, y + 1) not in sc:
#       h_cnt += 1
#       sc.add((x + 1, y + 1))

h, w, si, sj = map(int, input().split())
s = [list(input()) for _ in range(h)]
t = input()
si -= 1
sj -= 1
ans = 0
for c in t:
    ni, nj = si, sj
    if c == "L":
        nj -= 1
    if c == "R":
        nj += 1
    if c == "U":
        ni -= 1
    if c == "D":
        ni += 1
    if s[ni][nj] == "#":
        continue
    si, sj = ni, nj

    if s[si][sj] == "@":
        s[si][sj] = "."
        ans += 1

print(si + 1, sj + 1, ans)

"""
問題A_384：aaaadaa・・・勉強になった

10 b a
acaabcabba
aaaabaabba
逆を考える

"""

n, c1, c2 = input().split()
s = input()
ans = ""
for ss in s:
    if ss == c1:
        ans += c1
    else:
        ans += c2
print(ans)

"""
問題B_384：ARC Division

N回後ARCの高橋くんのレーティングを求める

ARC Div.1 では、コンテスト開始時のレーティングが1600 以上 2799 以下の参加者がレーティング更新の対象です。
ARC Div.2 では、コンテスト開始時のレーティングが 1200 以上 2399 以下の参加者がレーティング更新の対象です。

N=参加回数
A=成績
D=Divの番号
R=レーティング
T=コンテスト開始時のレーティング

更新対象、対象外
T+Ai = コンテスト更新後のレーティング
"""

N, R = map(int, input().split())
for i in range(n):
    D, A = map(int, input().split())
    if D == 1 and 1600 <= R <= 2799:
        R += A
    if D == 2 and 1200 <= R <= 2399:
        R += A
print(R)

"""
問題C_384：Perfect Standings（土日やる）
"""

"""
問題A_383：Humidifier 1・・・解けない（経過時間シミュレーション）

方針
水の量がマイナス値にならないようにmax関数で制御
前の時刻情報をpreにて保持
現在の水の量を計算しwaterに水を追加
"""

N = int(input())
pre, water = 0, 0
for i in range(N):
    T, V = map(int, input().split())
    water = max(0, water - (T - pre))  # 現在の水の量
    water += V  # 水を追加
    pre = T  # 前の時刻
print(water)


"""
A問題383_Humidifier 1（シミュレーション）・・・自力AC 2025/9/20
難易度19

★状態管理する為になんの変数が必要かを整理
現在の水の量を保持する変数 water
一つ前の時刻を保持する変数 pre_t

max(0, 現在の水の量-(現在の時刻-前の時刻))
負の値であっても最大0の扱いとする
"""

N = int(input())
water = 0
pre_t = 0

for i in range(N):
    time, v = map(int, input().split())
    water = max(0, water - (time - pre_t))
    water += v
    pre_t = time
print(water)

"""
問題B_383：Humidifier 2・・・解けない（土日やる）

マンハッタン距離：

(i, j) = あるマス
(i', j') = 加湿器が置かれたマス
|i - i'| + |j - j'|

加湿器を設置するマスは異なる2マスのみ
床に加湿器を設置する

#・・・机
.・・・床
"""

"""
問題A_382：Daily Cookie・・・経過シミュレーション

N=箱の個数
D=日数

N 個の箱のうち、
D日間が経過した後に空き箱であるものはいくつあるか求めてください
N - S + D
箱の数 - クッキーの数 + 日数

→結果の差分に注目する
@のマークを数える


"""

N, D = map(int, input().split())
S = input()
cnt = 0
for c in S:
    if c == ".":
        cnt += 1
print(cnt + D)

"""
問題B_382：Daily Cookie 2・・・解けた
文字列操作
"""

N, D = map(int, input().split())
S = list(input())
cnt = 0
for i in range(N - 1, -1, -1):
    if cnt < D and S[i] == "@":
        S[i] = "."
        cnt += 1
print("".join(S))


"""
問題A_381：11/22 String
"""
N = int(input())
S = input()
ans = ""

for i in range(N):
    print((N + 1) / 2 - 1)
    if i < (N + 1) / 2 - 1:
        ans += "1"
    elif i == (N + 1) / 2 - 1:
        ans += "/"
    else:
        ans += "2"

if ans == S:
    print("Yes")
else:
    print("No")


"""
問題B_381：1122 String・・・解けた

ちょうど2つの文字列が一致しているか
偶数：2*i
奇数：2*i+1
[2*i] == [2*i+1]


方針
奇数の時はNoを出力する

偶数の時に隣同士を比較し一致するか判定
一致しかつ重複していない場合のみセットに追加する
重複していた場合はNoを出力する

以上の条件をすべて通ったケースの身を1122文字列としYesと出力する

/・・・小数で比較する

"""

S = input()
if len(S) % 2 != 0:
    print("No")
    exit()
C = set()
for i in range(len(S) // 2):
    if S[2 * i] != S[2 * i + 1]:
        print("No")
        exit()
    elif S[2 * i] not in C:
        C.add(S[2 * i])
    else:
        print("No")
        exit()

print("Yes")


"""
問題C_381：11/22 SubString（土日やる）
"""

"""
問題380_A：123233・・・ちょっと難しい

昇順に並べ替えて122333と一致するか

＊＊＊＊各桁を取り出す＊＊＊＊＊
N > 0の間繰り返す
＊Nを10で割った余りを記録する・・・mod
＊Nを10で割り小数点を切り捨て・・・//

例）380から整数 3, 8 ,0を取り出す

380 % 10 = 0  | 380 // 10 = 38
38 % 10  = 8  | 38 // 10  = 3
3 % 10   = 3  | 3 // 10   = 0

→3, 0, 8


このケースがダメ
155555
444422
666666
"""
N = list(input())
C = set(N)
ans = 0

# 別解
N.sort()
if "".join(N) == "122333":
    print("Yes")
else:
    print("No")

for num in C:
    if N.count(num) != int(num):
        print("No")
        exit()
    print(type(num))
    if num == "1" or num == "2" or num == "3":
        ans += num

if ans == 6:
    print("Yes")
else:
    print("No")

"""
問題B_380：Hurdle Parsing・・・解けた

時間計算量：O(N)
方針
0番目の文字を'|'、'-'を'1'に置換する
'1'の間加算し続ける
'|'に一致した婆はループを抜け解答変数へ文字列連結し、
'|'を'0''を上書きする
|---|-|----|-|-----|
|111|1|1111|1|11111|

3 1 4 1 5
3 = 1 1 1
1 = 1
4 = 1 1 1 1
1 = 1
5 = 1 1 1 1 1
"""

S = input()
S = list(S.replace("-", "1").replace("|", "", 1))
ans, A = 0, 0
# 解答１（クソコード）
# while k < len(S) - 1:
#   while S[k] != '|':
#     A += int(S[k])
#     k += 1
#   ans += str(A) + ' '
#   A = 0
#   S[k] = '0'


# 別解（普通）
for i in range(len(S)):
    if S[i] != "|":
        A += int(S[i])
    else:
        S[i] = "0"
        ans += str(A) + " "
        A = 0
print(ans)

"""
問題A_379：Cyclic
a,b,c
b,c,a = 1,2,0
c,a,b = 2,0,1
"""

a, b, c = input()
print(b + c + a, c + a + b)

"""
問題B_379：Strawberries・・・解けた

N-K+1
方針
k*'0'のリストを作成し
Sが一致した時のみ連続している歯だと判定

'0'が連続しているかの判定
丈夫な歯か判定
イチゴを食べた回数を加算
"""

N, K = map(int, input().split())
S = input()
ans, cnt = [], 1
for c in S:
    if c == "X":
        cnt = 1
        continue
    if cnt < K and c == "O":
        cnt += 1
    else:
        cnt = 1
        ans.append("X")
print(len(ans))


"""
問題C_379：Sowing Stones（後でやる）
"""

"""
問題A_378：Pairing（場合の数）

同じ色のボールを 
2 つ選び両方捨てるという操作を最大何回行えるか

ボール4個の内、あり得る組合せは
・4色同じ (4, 0) = 2回
・2色同じ (2, 2) = 2回
・2色＋1色(2, 1) = 1回
・3色同じ (3, 1) = 1回
・4色違う (0, 0) = 0回

2色のペアになる最大値は
2, 1, 0の3パターン

方針
セットで重複をなくした上でループの中で元データより重複要素の件数を取得し、
2で割り件数を追加していく。

2で割った商が2なら1, 3なら1,4なら2 1なら0になる
2 + 2のペアなら = 2
2 + 0のペアなら = 1
0のペアなら     = 0

"""
A = list(map(int, input().split()))
C = set(A)
ans = 0
for a in C:
    ans += A.count(A) // 2
print(ans)

"""
問題B_378：Garbage Collection・・・解けない（土日やる）

問題の意味が分からない

ri  = day % qi
day = qi + ri
qi  = day - ri

次のゴミの回収日
(d - r + qi - 1) /qi * qi
"""

"""
問題A_377：Rearranging ABC
文字列にA B,Cが含まれているか
含まれているなら並べ替えた結果がABCになる理屈
"""

S = list(input())
S.sort()
print("Yes" if "".join(S) == "ABC" else "No")

"""
問題B_377：Avoid Rook Attack（グリッド）・・・解けた

コマが置けるマスの個数を求める
行 * 列

データ構造：リスト（文字列）
          セット（文字列型）*2 i,jの行列を保持
時間計算量：O(N^2)
  0 1 2 3 4 5 6 7
0|. . . # . . . .|
1|# . . . . . . .|
2|. . . . . . . #|
3|. . . . # . . .|
4|. # . . . . . .|
5|. . . . . . . .| OK
6|. . . . . . . .| OK
7|. . # . . . . .|

5,6行目：#なし

i行目に#がないこと
#があるj列目の情報を保持

#コマが置いている場所・・・j列目
(0, 3)
(1, 0)
(2, 7)
(3, 4)
(4, 1)
(7, 2)


この中に含まれていないj列目が置ける列
i = [0 ,1, 2, 3, 4, 7] = 5, 6
j = [3, 0, 7, 4, 1, 2] = 5, 6

5,6の通りは4つだけ
(5, 5)
(5, 6)
(6, 5)
(6, 6)

4個
   0 1 2 3 4 5 6 7
0｜. # . . . . . .|
1｜. . # . . # . .|
2｜. . . . # . . .|
3｜. . . . . . . .| OK
4｜. . # . . . . #|
5｜. . . . . . . .| OK
6｜. . . # . . . .|
7｜. . . . # . . .|

i = [0,1,2,4,6,7] = 3,5
j = [1,2,5,4,2,7,3,4] = 0,6

3, 5行が#を含まない
(3, 0)(3, 6)
(5, 0)(5, 6)
4個

方針：処理を分ける
1. 最初にコマ#が置かれている行列情報を格納
2. 保持した列情報の含まれていない行列の座標を全探索し個数を出す
"""

S = [list(input()) for _ in range(8)]
T = {i for i in range(8)}
N = len(S)
Si, Sj = set(), set()
for i in range(N):
    for j in range(N):
        if S[i][j] == "#":
            Si.add(i)
            Sj.add(j)

row_diff = T - Si
column_diff = T - Sj
print(len(row_diff) * len(column_diff))

"""
問題A_376：Candy Button（経過時間シミュレーション）
"""

N, C = map(int, input().split())
T = list(map(int, input().split()))
ans = 1
ti = T[0]
for i in range(N - 1):
    if C <= T[i + 1] - ti:
        ans += 1
        ti = T[i + 1]
print(ans)

"""
問題B_376：Hands on Ring・・・解けない

＊パーツを握る必要な操作回数の最小値を求める

L・・・s / R・・x / T・・・t
場合分けを減らす工夫
・L,Rの処理を共通化 → 関数化する
・s > tならsとtを入れ替える
・逆回り s < x < t：N-(t - s)
・そうでない：t - s

輪っかの処理は0開始がおすすめ
割った余りが0から開始したい
＝循環させるため


移動先にもう一方の手がない場合に指示のパーツに移動できる
"""


# from_（移動先）がng（LRがぶつからない）をto（通らない移動後）の距離を求める
def f(n: int, from_: int, to: int, ng: int) -> int:
    # 常にfrom_≦toの関係になる
    if from_ > to:
        from_, to = to, from_
    # 左回りの場合（from_からngを通らない距離を求める）
    if from_ < ng < to:
        return n + from_ - to
    else:
        # 右回りの場合
        return to - from_


N, Q = map(int, input().split())
L, R = 1, 2
ans = 0
for i in range(Q):
    H, T = input().split()
    T = int(T)
    # L,Rの処理を共通化（関数化）する
    if H == "L":
        ans += f(N, L, T, R)
        L = T
    else:
        ans += f(N, R, T, L)
        R = T
print(ans)


"""
問題A_375：Seats
"""
N = int(input())
S = input()
ans = 0
for i in range(N - 2):
    if S[i] == S[i + 2] == "#" and S[i + 1] == ".":
        ans += 1
print(ans)

"""
問題B_375：Traveling Takahashi Problem・・・解けた
座標の移動
"""


def f(A: int, B: int, X: int, Y: int) -> float:
    return sqrt((A - X) ** 2 + (B - Y) ** 2)


N = int(input())
A, B = 0, 0  # 原点の座標
ans = 0
for i in range(N):
    X, Y = map(int, input().split())
    ans += f(A, B, X, Y)
    A, B = X, Y
ans += f(A, B, 0, 0)
print(ans)

"""
問題A_374：Takahashi san 2
"""

S = input()
print("Yes" if S[-3:] == "san" else "No")

"""
問題B_374：Unvarnished Report・・・解けた
文字列長が同じ：◯
文字列長が違う：×
 |T|<|S|
T > Sの場合にS,Tを入れ替える

文字数がオーバーしている場合：
初めに文字数が最小の方をNに設定し
:スライスで文字数の範囲を末尾まで取得し、
等しければN＋1を出力

等しい
keyence = keyence

同じ文字数
abcde ≠ abedc

違う文字数
abcde ≠ abcdefg
abcdgzef ≠ abkd

"""
S, T = input(), input()
N = min(len(S), len(T))
ans = 0
# 等しい
if S == T:
    print(0)
    exit()
# 文字数がオーバーしている場合
if S[:N] == T[:N]:
    print(N + 1)
    exit()

for i in range(N):
    if S[i] != T[i]:
        ans = i + 1
        exit()
print(ans)

"""
問題A_373：September
"""
cnt = 0
for i in range(12):
    if i + 1 == len(input()):
        cnt += 1
print(cnt)

"""
問題B_373：1D Keyboard・・・解けた（ロジックを整理）

A に対応するキーを押してから、Z に対応するキーを押すまでの指の移動距離の合計として考えられる最小値を求める

ord関数を使い文字列を整数に変換。
変換リストを作る
MGJYIZDKSBHPVENFLQURTCWOAX
↓
文字列SのA-Zの並び順のindex(.indexしているのと同じ結果)
[24, 9, 21, 6, 13, 15, 1, 10, 4, 2, 7, 16, 0, 14, 23, 11, 17, 19, 8, 20, 18, 12, 22, 25, 3, 5]
"""
S = input()
K = [chr(ord("A") + i) for i in range(26)]

pre, ans = 0, 0
for key in K:
    index = S.index(key)  # iの位置を取得
    if key != "A":
        ans += abs(index - pre)
    pre = index
print(ans)

# 別解（解説）
# ord=文字列を整数に変換
s = input()
x = [0] * 26
for i in range(26):
    x[ord(s[i]) - ord("A")] = i

ans = 0
for i in range(25):
    ans += abs(x[i] - x[i + 1])
print(ans)

"""
問題A_372：delete .
"""

print(input().replace(".", ""))

"""
問題B_372：3^A・・・解けない

貪欲法を使い解答

10進法を3進法に変換していく

N
Σ 3^Ai = M
i = 0

Ai = 数列の要素
0 ≦ Ai ≦ 10

Ai（数列）が指数になるため0-10回のループになる
N進数変換は
余りを記録し、Nで割る
0になるまで繰り返す
"""

M = int(input())
A = []
while M > 0:
    a = 0
    while 3 ** (a + 1) <= M:
        a += 1
    A.append(a)
    M -= 3**a
print(len(A))
print(*A)


# 公式解法（理解できていない）
for k in range(11):
    A += [k] * (M % 3)  # ここで新しい数列を作っている
    M //= 3
print(len(A))
print(*A)


"""
問題A_371：Jiro（場合分け）

このロジックは整理できる

A == B or B == C
< < < = B
> > > = B

A != B
> < < = A
< > > = A

B != C = C
< < >
< < >


全部で6パターン（左右*3=6）
サンプル
< < <  a < b < c = B
< < >  a < c < b = C
> < <  b < a < c = A  A > B, A < C, B < C
< < >  a < c < b = C
> > >  c < b < a = B
< > >  c < a < b = A

これ矛盾したパターン（考慮不要）
> < >  b < a < b = C
< > <  a < b < c = B
"""

# 簡明なコード（ここに今の自分の足りない要素が詰まっている（場合分け））
AB, AC, BC = input().split()
if AB != AC:
    print("A")
if AB == BC:
    print("B")
else:
    print("C")

S = ""
S = AB + AC + BC

if S == "><<":
    print("A")
if S == "<>>":
    print("A")
if S == "<<<":
    print("B")
if S == ">>>":
    print("B")
if S == "<<>":
    print("C")
if S == "<<>":
    print("C")


# クソコード（場合分けの解法）
# ans = 'A'
# if AB == '<':
#   ans = 'B'

# if ans == 'A': # A > B
#   if AC == '<': # A < C, B < C
#     print(ans)
#     exit()
#   elif BC == '>':# A > C, B < C
#     ans = 'B'
#   else:
#     ans = 'C'
# elif ans == 'B': # A < B
#   if AC == '>': # A < C, B > C
#     ans = 'A'
#   elif BC == '>': # A < C, B > C
#     ans = 'C'
# print(ans)

"""
問題B_371：解けた

重複を考慮した問題
"""
N, M = map(int, input().split())
C = set()
for _ in range(M):
    A, B = input().split()
    if B == "M" and A not in C:
        C.add(A)
        print("Yes")
    else:
        print("No")

"""
問題A_370：Raise Both Hands
"""

L, R = map(int, input().split())
if L == 1 and R == 0:
    print("Yes")
elif L == 0 and R == 1:
    print("NO")
else:
    print("Invalid")

"""
問題B_370：Binary Alchemy・・・解けない？？？

＊現時点での元素の管理が重要
求めたい答えには「x」と定義

問題の意味がわからない
→イメージが出来ない時は問題文の通りに実装する思考に切り替える

＊現時点での元素番号をxで管理している
"""

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
x = 1
for i in range(1, N + 1):
    if x >= i:
        x = A[x - 1][i - 1]
    else:
        x = A[i - 1][x - 1]
print(x + 1)

"""
問題A_369：369（等差数列）・・・解けない

解法1
-100〜100までの全探索で等差数列を調べるのはめんどくさい

解法2
場合分けをし必要な条件を洗い出す
x,A,B
A,x,B
A,B,x


＊＊場合分けを考える

隣り合う２つの差が全て同じ
等差の条件：
A, B, x
p - q = r - q

等差数列は並べ替えても等差は同じ


等差数列とは隣り合った2つの整数の差が同じ
q-p = r-q→・・・等差数列


3,5,7
x, A, Bの場合
等差数列＝A1,A2,A3
A2 - A1 = A3 - A2


この数式でxが求められる
A - x = B - A
x = 2A - B・・・パターン①(x,A,B)

B - A = x - B
x = 2B - A・・・パターン②(A,B,x)

x - B = A - x
2x = A + B
両辺を２で割る
x = (A + B) / 2 % 2 = 0・・・パターン③(B,x,A) ※偶数の時だけ

例）
A = 5, B = 7

x = 2*5 - 7
x = 10-7
x = 3

x = 2*7-5
x = 14-5
x = 9

x = 5+7/2
x = 6
"""
# 場合分け後
A, B = map(int, input().split())
if A == B:  # 2つの整数の差は同じ
    print(1)
elif (A + B) % 2 == 0:
    print(3)
else:
    print(2)


"""
問題B_369：Piano 3・・・解けた

右手の数列と左手の数列を配列に分けることで
疲労度の計算の差の処理を共通化できる

シミュレーション
前の値の保持
計算の累積
問題文の理解

8            疲労度  キー
75 L 75-22 = 53＊  75＊
45 R 45-26 = 19＊  45＊
ここまでは多分合っている

72 R 72-45 = 27    72
81 R 81-72 = 9     81
47 L 47-75 = 28    47
29 R 29-81 = 52    29

L=103

189
"""

N = int(input())
L, R = 0, 0
ans = 0
for i in range(N):
    A, T = input().split()
    A = int(A)
    if T == "L" and L != A:
        if L != 0:
            ans += abs(A - L)
        L = A
    elif T == "R" and R != A:
        if R != 0:
            ans += abs(A - R)
        R = A
print(ans)

# 別解（公式）
pos = [-1, -1]  # left:0 right:1
for i in range(N):
    A, T = input().split()
    A = int(A)
    hand = 0 if T == "L" else 1
    if pos[hand] != -1:
        ans += abs(pos[hand] - A)
    pos[hand] = A
print(ans)

"""
問題A_368：Cut

文字列操作
スライスを利用し範囲指定
"""

N, K = map(int, input().split())
A = input().split()
print(*A[N - K :], *A[: N - K])

"""
問題B_368：Decrease 2 max elements・・・解けた
"""

N = int(input())
A = list(map(int, input().split()))
INF = 10**9
for ans in range(INF):
    A.sort(reverse=True)
    if A[1] <= 0:
        print(ans)
        break
    A[0] -= 1
    A[1] -= 1


"""
問題A_367：Shout Everyday・・・場合分け・・・解けない

A：起きている時間
B：寝ている時間
C：起床する時間

場合分け
日付をまたぐか・またがないか

日付
またがない：B < C
またぐ   ：C < B

Aが愛を叫ぶことができる条件
B < C < A＝Yes
B < A < C＝No

日付をまたがない場合：B < C
AがBとCの間に含まれていたらNo
 B < C < A＝Yes
 B < A < C＝No

日付をまたいだ場合： C < B
CからBの間にAがいるか
C < A < B＝Yes
A < C < B＝No

"""
A, B, C = map(int, input().split())
# 日をまたがない場合
if B < C:
    print("No" if B < A < C else "Yes")
# 日をまたぐ場合
else:
    print("Yes" if C < A < B else "No")


"""
問題B_367：Cut .0・・・解けない

冷静になれば解けた問題
ACしなさすぎると迷走しがち

文字列として処理する
場合分け
末尾が0か0ではないか

末尾が0ではない→そのまま出力
末尾が0でなくなるまで0を削除
小数点以下の部分について末尾に0をつけない

ループ後に末尾が'.'なら'.'を削除し出力
"""

X = list(input())
while X[-1] == "0":
    X.pop()
if X[-1] == ".":
    X.pop()
print("".join(X))

"""
問題A_366：Election 2・・・土日やる
"""

N, T, A = map(int, input().split())
print("No" if abs(T - A) < N - (T + A) else "Yes")


"""
問題B_366：・・・Vertical Writing（グリッド）

M行 * N列の2次元配列をとる
M＝文字列の最大長を取得

外側のループ N
内側のループ 文字列長
(j, N - 1 - i)が入れ替え後の座標

末尾に'*'がなくなるまで＊を削除する
最終結果を出力
"""

N = int(input())
S = [list(input()) for _ in range(N)]
m = 0
# 文字列の最大値を取得
for s in S:
    m = max(m, len(s))
grid = [["*"] * N for i in range(m)]

for i in range(N):
    for j in range(len(S[i])):
        grid[j][N - 1 - i] = S[i][j]

for row in grid:
    while row[-1] == "*":
        row.pop()
    print("".join(row))


"""
問題A_365：Leap Year

場合分け：
4で割り切れない = 365
400で割り切れない = 365

4の倍数かつ100で割り切れない = 366
4の倍数かつ400で割り切れる = 366
"""

Y = int(input())
if Y % 4 == 0 and (Y % 100 != 0 or Y % 400 == 0):
    print(366)
else:
    print(365)

"""
問題B_365：Second Best・・・解けた

2番目に大きい値を取得する
リストを昇順に並び替え末尾から2番目のindexを取得し+1する
"""

N = int(input())
A = list(map(int, input().split()))
print(A.index(sorted(A))[-2] + 1)

"""
問題A_364：Glutton Takahashi・・・解けない（シミュレーション）

一個前が甘かったか否か
最後の一個は考えない
N - 2以下の中で隣同士が'sweet'の時はNo
それ以外はYes
"""

N = int(input())
S = [input() for _ in range(N)]
for i in range(N - 2):
    if S[i] == S[i + 1] == "sweet":
        print("No")
        exit()
print("Yes")


"""
問題B_364：Grid Walk・・・解けない（土日やる）
8割ほぼ解けた

H * W のグリッド 6マス
(Si, Sj)＝現在いるマス（1, 0）

現在のマスから移動していく
＊マスの範囲外の処理の判定を入れる


1.マスの存在チェック
2.マスが存在する場合に'.'かどうか

行＝H
列＝W

＊＊範囲外のかどうかの処理の判定方法を復習
マスの存在チェック + 白マス判定
H,Wも現在の位置を差し引くことに注意！！

U：行 -1 Si > 0 and Si-1のマスが'.'
D：行 +1 Si < H - 1 and Si+1のマスが'.'
L：列 -1 Sj > 0 and Sj - 1のマスが'.'
R：列 +1 Sj < W - 1 and Sj+1のマスが'.'

"""

H, W = map(int, input().split())
Si, Sj = map(int, input().split())
C = [list(input()) for _ in range(H)]
S = input()
Si -= 1
Sj -= 1  # 配列の添え字に合わせる

for c in S:
    if c == "U" and Si > 0 and C[Si - 1][Sj] == ".":
        Si -= 1
    if c == "L" and Sj > 0 and C[Si][Sj - 1] == ".":
        Sj -= 1
    if c == "R" and Sj < W - 1 and C[Si][Sj + 1] == ".":
        Sj += 1
    if c == "D" and Si < H - 1 and C[Si + 1][Sj] == ".":
        Si += 1
print(Si + 1, Sj + 1)


"""
問題A_363：Piling Up

最適なのは計算で求める
100の倍数ごとに上がっていることに注目する
R//100で解ける

100 - R % 100
100 - 123 % 100
100 - 23 = 77
"""

# 計算
R = int(input())
target = (R // 100 + 1) * 100
print(target - R)

# 場合分け
if R < 100:
    ans = 100 - R
elif R < 200:
    ans = 200 - R
elif R < 300:
    ans = 300 - R
print(ans)

"""
問題B_363：Japanese Cursed Doll・・・解けた
＊髪の長さがT以上になるのがP人以上になる日数を求める

降順に並べ替えをしP回繰り返す
配列の要素がTより大きくなるまで要素を+1加算していく
配列参照外にならないように循環させる
"""

N, T, P = map(int, input().split())
L = list(map(int, input().split()))
L.sort(reverse=True)
cnt = 0
for i in range(P):
    ans = 0
    while cnt <= P:
        if L[i] < T:
            L[i] += 1
            ans += 1
        else:
            cnt += 1
            break
print(ans)


"""
問題A_362：Buy a Pen
(R, G),(R,B),(G, B)

"""
R, G, B = map(int, input().split())
C = input()
ans = 0
if C == "Red":
    ans = min(G, B)
elif C == "Green":
    ans = min(R, B)
else:
    ans = min(R, G)
print(ans)

"""
問題B_362：Right Triangle・・・解けない（6/24やる）
直角三角形であるかを判定する

三平方の定理を使えば解答できる
"""


"""
問題A_361：Insert
"""

NN, K, X = map(int, input().split())
A = list(map(int, input().split()))
A.insert(K, X)
print(*A)


"""
問題A_360：A Healthy Breakfast
味噌汁の左側にご飯
RMS
RSM
SRM
"""

S = input()
print("Yes" if S[0] == "R" or S[1] == "R" and S[2] == "M" else "No")


"""
問題B_360：Vertical Reading・・・解けない（土日やる）
"""

"""
問題A_359：Count Takahashi
"""

N = int(input())
S = [input() for _ in range(N)]
print(S.count("Takahashi"))


"""
問題B_359_：Couples・・・解けた
boolの結果が0,1になる
条件が成立した時はカウントされる
"""

N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(2 * N - 2):
    ans += A[i] != A[i + 1] and A[i] == A[i + 2]
print(ans)


"""
問題A_358：Welcome to AtCoder Land
"""

S, T = input().split()
print("Yes" if S == "AtCoder" and T == "Land" else "No")


"""
問題B_358：Ticket Counter・・・意味がわからない（解けない）・・・土日やる

i番目の人が購入手続き中かそうでないかの判定を場合分けする必要がある。
場合分けができないz

"""

# 公式解法
n, a = map(int, input().split())
t = list(map(int, input().split()))
pre = 0
for i in range(n):
    ans = max(pre, t[i]) + a
    print(ans)
    pre = ans


"""
問題A_357：Sanitize Hands（シミュレーション）・・・解けない

今何人目か
あと何本か
"""
N, M = map(int, input().split())
H = list(map(int, input().split()))
ans = 0
for h in H:
    if M < h:
        break
    M -= h
    ans += 1
print(ans)


"""
問題B_357：Uppercase and Lowercase・・・解けた
正規表現で大文字を取得し文字列長から大文字の個数を引き
小文字の個数を出し、大文字と小文字の数を比較し判定する
"""

S = input()
ans = re.findall("[A-Z]", S)
n = len(ans)
ans = S.upper() if len(S) - n < n else S.lower()
print(ans)


"""
問題A_356：Subsegment Reverse・・・解けない（土日やる）

リストのスライスで範囲指定し要素を上書き
"""

# 解法
N, L, R = map(int, input().split())
A = list(range(1, N + 1))
A[L - 1 : R] = A[L - 1 : R][::-1]
print(*A)


"""
問題B_356：Nutrients・・・解けない

問題文の意味がわからない（整理ができなかった）
"""

N, M = map(int, input().split())
A = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(N)]

for j in range(M):
    s = 0
    for i in range(N):
        s += X[i][j]
    if s < A[j]:
        print("No")
        exit()
print("Yes")


"""
問題A_355：Who Ate the Cake?

場合分け
1+2+3=6になるということは
6-(A+B)を余りが1,2,3のどれからになる

AとBが記憶している人が同じなら犯人を2人から絞れないので-1
AとBが記憶している人が別人なら
"""

A, B = map(int, input().split())

if A == B:
    print(-1)
    exit()
elif A != B:
    print(6 - A - B)

"""
問題B_355：Piano2・・・あと少しで解けた（難易度109）

隣り合う要素の判定
in演算子でも可能！！
iかつi+1がinで含まれていたら隣り合っている
"""

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = A + B
C.sort()

for i in range(N + M - 1):
    if C[i] in A and C[i + 1] in A:
        print("Yes")
        exit()
print("No")

"""
問題354：AtCoder Janken 2・・・解けた
"""

N = int(input())
ans_, t = [], []
for _ in range(N):
    S, C = input().split()
    ans_.append(S)
    t.append(int(C))

print(sorted(ans_)[sum(t) % N])


"""
問題A_354：Exponential Plant・・・勉強になった（解けた）シミュレーション
"""

H = int(input())
plant, ans = 0, 1
for i in range(H):
    plant = plant * 2 + 1
    if H < plant:
        break
    else:
        ans += 1
print(ans)

"""
問題A_353：Buildings
"""

N = int(input())
H = list(map(int, input().split()))
for i in range(1, N):
    if H[0] < H[i]:
        print(i + 1)
        exit()
print(-1)

"""
問題B_353：AtCoder Amusement Park・・・解けない（土日やる）
"""


N, K = map(int, input().split())
A = list(map(int, input().split()))
seat = K
ans = 0
for i in range(N):
    if seat < A[i]:
        seat = K
        ans += 1
    seat -= A[i]
print(ans)


"""
問題A_352：AtCoder Line

N X Y Z
N=駅の数
移動の間に高橋君が乗っている電車が駅 
Z に停車することがあるか判定してください。

場合分け
X < Y：上り列車
x < z < y

X > Y：下列車
y < z < x
"""

N, X, Y, Z = map(int, input().split())
if X < Y:
    print("Yes" if X < Z < Y else "No")
else:
    print("Yes" if Y < Z < X else "No")

"""
問題B_352：Typing（シミュレーション）・・・解けない

Sの文字列の何文字目がまでが入力されたかを表す変数が必要
文字列Tの前から順に調べる
文字列の比較
"""

S = input()
T = input()
si = 0
for i in range(len(T)):
    if S[si] == T[i]:
        print(i + 1, end=" ")
        si += 1


"""
問題A_351：The bottom of the ninth
"""

A = list(map(int, input().split()))
B = list(map(int, input().split()))
print((sum(A) - sum(B)) + 1)


"""
問題B_351：Spot the Difference・・・解けた（難易度34）

A,Bのグリッドを走査して異なる文字列を発見する
"""

N = int(input())
A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if A[i][j] != B[i][j]:
            print(i + 1, j + 1)
            exit()


"""
問題A_350：Past ABCs

ABC000に注意！
316は含まない
かつ
1以上350未満の範囲ならYes,それ以外はNo
"""

S = input()
print("Yes" if S[-3:] != "316" and 1 <= int(S[-3:]) < 350 else "No")


"""
問題B_350；Dentist Aok（シミュレーション）・・・解けた（難易度45）

N＝歯の本数
Q＝治療回数

すべての治療が終わった後高橋くんに生えている歯の本数を求める

穴Tiに歯が生えている場合、穴Tiから歯を抜く
穴Tiに歯が生えていない場合、穴Tiに歯を生やす

すでに抜いた歯の情報が必要
"""

N, Q = map(int, input().split())
T = list(map(int, input().split()))
C = set()
ans = N
for t in T:
    # 歯を抜く
    if t not in C:
        C.add(t)
        ans -= 1
    # 歯を生やす
    else:
        C.remove(t)
        ans += 1
print(ans)


"""
問題A_349：Zero Sum Game・・・解けない（シミュレーション）
合計が0になる性質を利用する

4
1 -2 -1
0  1  2

A1+A2+A3+x=0
1+(-2)+-1+x
-2 + x = 0
x = 2
"""

N = int(input())
A = list(map(int, input().split()))
print(-sum(A))


"""
問題B_349：Commencement・・・（難易度89）ほぼ解けた

それぞの文字が文字列中に現れる回数を調べる
2ステップに分けて考える

1.それぞれの文字の分布を求める
2.1.の情報からさらに登場回数のペアの分布を求める
2:2→全部が2のペアならOK
"""

S = input()
C = set(S)  # 重複を除く
l = [S.count(s) for s in C]  # 文字列の分布を取る
cnt = [l.count(i) for i in l]  # さらにペアの分布を取る
print("Yes" if all(c == 2 for c in cnt) else "No")

"""
問題A_348：Penalty Kick
"""

N = int(input())
ans = ""
for i in range(1, N + 1):
    ans += "x" if i % 3 == 0 else "o"
print(ans)

"""
問題B_348：Farthest Point（難易度79）・・・解けない（土日やる）

今の自分では解けない

整数同士で比較させる
ルートにすると小数になるため誤差が発生し正しい最小値を得られない
"""


# 他の人の解法（理解できていないので要復習）
def sq(x):
    return x * x


N = int(input())
X, Y = [0] * N, [0] * N
# x,yの座標を準備
for i in range(N):
    X[i], Y[i] = map(int, input().split())

for i in range(N):
    m, id = 0, -1
    for j in range(N):
        if i == j:
            continue
        # 最大の距離を計算
        d = sq(X[i] - X[j]) + sq(Y[j] - Y[i])
        if d > m:
            m, id = d, j
    print(id + 1)


"""
問題A_347：Divisible
"""

N, K = map(int, input().split())
A = list(map(int, input().split()))
for x in A:
    if x % K == 0:
        print(x // K, end=" ")

"""
問題B_347：SubString

部分文字列を列挙し重複を除いて個数を数えること
yay
y, ya, yay, a,ay, y
重複を除く
y,ya,yay,a,ay=５種類


"""
# 他の人の解法
S = input()
N = len(S)
st = set()
for i in range(N):
    for j in range(i, N):
        st.add(S[i : j + 1])
print(len(st))


"""
問題A_346：Adjacent Product
"""

N = int(input())
A = list(map(int, input().split()))
for i in range(N - 1):
    print(A[i] * A[i + 1], end=" ")


"""
問題A_345：Leftrightarrow・・・解けた（難しい）勉強になった
"""

S = input()
cnt = S.count("=")
ok = True if S[0] == "<" and S[-1] == ">" else False
print("Yes" if ok and len(S) - 2 == cnt else "No")


"""
問題B_345：Integer Division Returns

a/bの小数点以下を切り上げた整数を求めることを切り上げ徐算
a/b = (a + b - 1) /bが成り立つ
→(a +b -1) / b

a = X b = 10

結論
★(X + 9) // 10
境界値をずらすことで切り上げ除算ができる


Python：
// → 切り捨て（整数除算）
/  → 浮動小数


math
切り上げ：ceil
切り捨て：floor

四捨五入：round
"""

# 公式の解法
X = int(input())
print((X + 9) // 10)

"""
問題A_344：Spoiler・・・勉強になった

|および|の間の文字列を削除した文字列を出力する
|の位置を特定後その範囲範囲内を削除する
"""

S = list(input())
index = [i for i in range(len(S)) if S[i] == "|"]
S[index[0] : index[1] + 1] = []
print("".join(S))

"""
問題B_344：Delimiter・・・解けた

入力のNが与えられない
どう入力の終了を判断するか
末尾が0になることが保証されているため
0を終了判断条件とする
"""

A = []
line = -1
while line != 0:
    line = int(input())
    A.append(line)
for i in A[::-1]:
    print(i)

"""
問題A_343：Wrong Answer

答えを0,1で答える
0以外なら0
0なら1
"""

A, B = map(int, input().split())
# print(1 if A+B == 0 else 0)
print((A + B) ^ 1)  # a,bの一方だけが1なら1, それ以外は0になる

"""
問題B_343：Adjacency Matrix・・・解けた
"""

N = int(input())
for i in range(N):
    ans = ""
    A = map(int, input().split())
    for j, x in enumerate(A):
        if x == 1:
            ans += str(j + 1) + " "
    print(ans)

"""
問題A_342：Yay!

方針
昇順に並べ替える
先頭と2番目が隣接している場合は末尾のindexを取得、
隣接していなければ先頭のindexを取得
"""

S = list(input())
l = sorted(S)
ans = l[-1] if l[0] == l[1] else l[0]
print(S.index(ans) + 1)

"""
問題B_342：Which is ahead?・・・解けた

時間計算量：O(N)
データ構造：辞書
"""

N = int(input())
P = list(map(int, input().split()))
K = {}
# 頻度分布を取る
for i in range(N):
    K[P[i]] = i
Q = int(input())

for i in range(Q):
    A, B = map(int, input().split())
    index = min(K[A], K[B])
    print(P[index])

"""
問題A_341：Print 341
1、0を交互に出力する
"""

N = int(input())
print("10" * N + "1")

"""
問題B_341：Foreign Exchange・・・解けない（シミュレーション）（難易度163）（土日やる）
"""

# 他の人の解法
N = int(input())
A = list(map(int, input().split()))
for i in range(N - 1):
    s, t = map(int, input().split())
    A[i + 1] += A[i] // s * t
print(A[-1])

"""
問題A_340：Arithmetic Progression（等差数列）
初項（A）、末項（B）、公差（D)が与えらえる
"""

A, B, D = map(int, input().split())
ans_3 = [A]
while A < B:
    A += D
    ans_3.append(A)
ans_3.append(B)
print(*ans)

"""
問題B_340：Append（シミュレーション）・・・解けた
"""

Q = int(input())
A = []
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        A.append(x)
    else:
        print(A[-x])

"""
問題A_339：TLD
"""

S = input()
print(S.split(".")[-1])

"""
問題B_339：Langton's Takahashi（難易度251）・・・解けない（土日やる）
グリッド＆シミュレーション

必要な情報
i, j 墓橋くんの場所の座標
grid グリッドの状態
v 移動方向（0,1,2,3）
"""

"""
問題338_Capitalized?

文字列スライスで取得する
S[1:].islower()
capitalize()で文字列を先頭を大文字にそれ以外を小文字に変換し
＝＝で比較する
"""

S = input()
s = re.findall("[a-z]", S)
ans = "Yes" if S[0].isupper() and len(s) == len(S) - 1 else "No"
print(ans)

"""
問題338_Frequency・・・解けた

各文字列の頻度分布を取る
文字列を昇順に並べ替えた後、値が最大値のキーを取得する
"""

S = list(input())
S.sort()
ans, pre = 0, 0
K = {}
for c in S:
    K[c] = S.count(c)

for k, v in K.items():
    if pre < v:
        pre = max(pre, v)
        ans = k
print(ans)


"""
問題A_337_Scoreboard
"""

N = int(input())
aoki, takahashi = 0, 0
for i in range(N):
    X, Y = map(int, input().split())
    takahashi += X
    aoki += Y

ans = "Aoki"
if aoki == takahashi:
    ans = "Draw"
elif aoki < takahashi:
    ans = "Takahashi"

print(ans)

"""
問題B_337_Extended ABC・・・解けた
難易度97

方針
A B,Cの頻度分布を取る
その上で文字列を掛け算（最大文字列長が100以下かつ個々の文字列が100を超えることはないため
メモリエラーにならない）

a + b + cの文字列とSが等しい場合だけYes、等しくなければNoとする

別解
文字列を昇順でソートして元の文字列と一致すればYes,そうでなければNo
"""

S = input()
Sa, Sb, Sc = "A", "B", "C"
a, b, c = 0, 0, 0
for i in range(len(S)):
    if S[i] == "A":
        a += 1
    if S[i] == "B":
        b += 1
    if S[i] == "C":
        c += 1

Sa, Sb, Sc = Sa * a, Sb * b, Sc * c
ex_S = Sa + Sb + Sc
print("Yes" if ex_S == S else "No")

# 別解（並べ替え）
s = sorted(S)
print("Yes" if s == S else "No")

"""
問題A_336_Long Looong
"""

N = int(input())
print("L" + "o" * N + "ng")

"""
問題B_336_CTZ・・・解けた
難易度27
"""

N = int(input())
ans, N = 0, bin(N)
for i in N[::-1]:
    if i != "0":
        break
    ans += 1
print(ans)

print(bin(N)[::-1].find("1"))

"""
問題A_335_202<s>3</s>
"""

S = list(input())
S[-1] = "4"
print("".join(S))

"""
問題B_335_Tetrahedral Number・・・解けた（全探索）
難易度52
要修正：O(N^2)へ修正できそう
"""
N = int(input())

for x in range(N + 1):
    for y in range(N + 1):
        for z in range(N + 1):
            if x + y + z <= N:
                print(x, y, z)

# 別解
N = int(input()) + 1
for x in range(N):
    for y in range(N - x):
        for z in range(N - x - y):
            print(f"{x} {y} {z}")

"""
問題A_334_Christmas Present 
"""

B, G = map(int, input().split())
print("Glove" if B < G else "Bat")

"""
問題B_334_Christmas Trees・・・解けない（要復習）
難易度479
"""

# evimaさん解法
A, M, L, R = map(int, input().split())
l = L + (A - L) % M
r = R - (R - A) % M
print((r - l) // M + 1)

"""
問題A_333_Three Threes
"""

N = int(input())
print(str(N) * N)

"""
問題B_333_Pentagon・・・解けない（要復習）
難易度89

線分の長さが短いか長以下をどう判定する？

円周上の距離を求める
正五角形の点A,B,C,D,Eを0,1,2,3,4に変換

五角形の5点（A, B, C, D, E）を円形に並べて、2点間の「最短距離」を数値として比べる

時計回りと反時計回りの最短距離をminで比べている
その為、5-Nをし、反時計回りの距離を求めている

線が長いか短いかでそれぞれの線の長さが等しいかを判定
"""

x = "ABCDE"  # index化


# 線が長いか短いかの判定
# 長い：2, 3
# 短い：1, 4
def f_(x: int, y: int) -> bool:
    diff = abs(x - y)
    return diff == 2 or diff == 3


A, B = map(x.index, input())
C, D = map(x.index, input())

print("Yes" if f_(A, B) == f_(C, D) else "No")
# N = abs(A - B)
# N = min(N, 5 - N)
# M = abs(C - D)
# M = min(M, 5 - M)
# if N == M: print('Yes')
# else: print('No')

"""
問題A_332_Online Shopping
"""

N, S, K = map(int, input().split())
ans = 0
for i in range(N):
    P, Q = map(int, input().split())
    ans += P * Q
print(ans if ans >= S else ans + K)

"""
問題B_332_Glass and Mug・・・解けない
難易度76
シミュレーション問題

min(変化量、残りキャパ)
注げる最大の水の量＝マグの残量 or グラスの空き容量、のどちらか小さい方

注げる量 = min(マグの残量, グラスの空き容量)
         = min(mag, G - glass)

状態の更新を一つずつ行う
"""

K, G, M = map(int, input().split())
glass, mag = 0, 0
for _ in range(K):
    if glass == G:
        glass = 0
    elif mag == 0:
        mag = M
    else:
        pour = min(mag, G - glass)
        glass += pour
        mag -= pour
print(glass, mag)

"""
問題A_331_Tomorrow

場合分け
年を跨いでいるか：M=mかつD＝d
月を跨いでいるか：D＝d
日だけ加算か：それ以外
"""

M, D = map(int, input().split())
y, m, d = map(int, input().split())

# 年を跨いでいるか
if M == m and D == d:
    y += 1
    m, d = 1, 1
# 月を跨いでいるか
elif D == d:
    m += 1
    d = 1
# 日だけ加算
else:
    d += 1
print(y, m, d)

"""
問題B_331_Buy One Carton of Milk・・・解けない（全探索）

N^3通り回す
"""
N, S, M, L = map(int, input().split())
ans = 1e6
for i in range(N + 1):
    for j in range(N + 1):
        for k in range(N + 1):
            if 6 * i + 8 * j + 12 * k >= N:
                ans = min(ans, S * i + M * j + L * k)
print(ans)


"""
問題C_331_Sum of Numbers Greater Than Me・・・解けない（要復習）
難易度288
"""

# 他の人の解法
N = int(input())
A = list(map(int, input().split()))
total = sum(A)
R = [0] * (10**6 + 1)
for a in A:
    R[a] += a

for i in range(1, len(R)):
    R[i] += R[i - 1]

print(*[total - R[a] for a in A])

"""
問題A_330_Counting Passes
"""

N, L = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for a in A:
    if L <= a:
        ans += 1
print(ans)

"""
問題B_330_Minimize Abs 1・・・解けない（問題の意味が不明）
難易度118
区間L,Rの中で最もA[i]に近いXiを求める

場合分け
A[i]＜L：L
R ≦ A[i] ≦ L：A[i]
A[i]＞R：R

x を L 以上 R 以下に丸める
min(max(x, L), R

min(), max()の本質＝
場合分け（条件分岐）を数式で表す為の道具
"""

N, L, R = map(int, input().split())
A = list(map(int, input().split()))
ans = [min(max(x, L), R) for x in A]
print(*ans)


"""
問題A_329_Spread
"""

print(*[s for s in input()])

S = input()
print(" ".join(S))

"""
問題B_329_Next・・・解けた
"""

N = int(input())
A = list(map(int, input().split()))
max_val = max(set(A))
ans = [c for c in A if max_val != c]
print(max(ans))

# ２番目に大きい数を求める
print(sorted(set(A), reverse=True)[1])

"""
問題A_328_Not Too Hard 
"""

N, X = map(int, input().split())
A = list(map(int, input().split()))
print(sum(a if a <= X else 0 for a in A))

"""
問題B_328_11/11
"""


"""
C問題_AntiDivision・・・解けない
難易度518


A以上B以下の範囲の範囲でCでもDでも割り切れない整数の数を求める

→X以下の中でCでもDでも割り切れる個数を個数を求め全体から引き
最小公倍数を足す

Cの倍数の個数＝B/C
Dの倍数の個数＝B/D

CでもDでも割り切れる個数を求める
＝CとDの最小公倍数

最小公倍数＝（C＊D）// 最大公約数（C,D）
最大公約数＝D％C==0になった時点のCの値（ユークリッドの互余法）

最終的に
B - B/C - B/D + B/最小公倍数

最小公倍数を求める方針は合っていた。

"""


A, B, C, D = map(int, input().split())


# ユークリッドの互除法（最大公約数を求める）
def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)


# CでもDでも割り切れない個数を求める
def not_count_multiple(n, c, d):
    # 最小公倍数を求める
    lcm = c // gcd(c, d) * d
    return n - (n // c) - (n // d) + n // lcm


A1 = not_count_multiple(B, C, D)
A2 = not_count_multiple(A - 1, C, D)

print(A1 - A2)



"""
問題A_114_753
"""

X = int(input())
print("YES" if X in (7, 5, 3) else "NO")


"""
B問題114_754
難易度148
"""
S = input()
ans = 10**6
for i in range(len(S) - 2):
  ans = min(ans ,abs(753 - int(S[i : i + 3])))
print(ans)



"""
C問題114_753数


| 関数             | 意味            | 重複 | 順序    |
| -------------- | ------------- | -- | ----- |
| `product`      | デカルト積（繰り返し選択） | OK | 区別する  |
| `permutations` | 順列（並べ替え）      | NG | 区別する  |
| `combinations` | 組合せ           | NG | 区別しない |



重複あり順序あり
itertools.product・・・直積

「要素を繰り返し取り出して、組み合わせる」イメージ。
repeat を指定すると「同じ集合から何回も選ぶ」ことができる。
”同じ数字を繰り返し使える”


itertools.permutations・・・順列を作る（並べ替え）
（リスト、長さr）長さrの順列を作る
nPr (n-r)!

”同じ数字を繰り返しは使えない”

itertools.combinations・・・組合せ（順番を区別しない）
nCr n!/r! * (n - r)!
"""

N = int(input())
digits = ["3", "5", "7"]
ans = 0

def dfs3(cur_s):
    global ans
    if len(cur_s) >= 3:
        if "3" in cur_s and "5" in cur_s and "7" in cur_s:
            if int(cur_s) <= N:
                ans += 1
    if len(cur_s) >= len(str(N)):
        return
    
    for d in digits:
        dfs3(cur_s + d)


dfs3("")
print(ans)




"""
C問題007_幅優先探索・・・解けない
難易度1024
典型グリッドの走査、４近傍（上下右左）の移動の仕方
"""

R,C= map(int, input().split())
sy, sx = map(int, input().split()) # 開始地点
gy, gx = map(int, input().split()) # ゴール
H = [input() for _ in range(R)] # 二次元座標
# -1:未訪問 0:訪問済み
dist = [[-1] * C for _ in range(R)] # 頂点が訪問済みかどうかを管理

# 0-indexedに変更
sy -= 1; sx -= 1
gy -= 1; gx -= 1

# 探索待ちのマスを入れるキューを準備
que = deque()
que.append([sy, sx])
dist[sy][sx] = 0 # 開始地点を訪問済みに変更

# BFS キューを取り出しながら探索
while que:
  y, x = que.popleft()
  # 上下左右のマスを確認
  for dy, dx in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
    # マスが存在しない場合は無視
    if not (0 <= dy < R and 0 <= dx < C):
      continue
    # 壁だった場合も無視
    if H[dy][dx] == "#":
      continue
    # マスが未訪問だった場合は距離を更新しキューに入れる
    if dist[dy][dx] == -1:
      dist[dy][dx] = dist[y][x] + 1
      que.append([dy, dx])

print(dist[gy][gx])