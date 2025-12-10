import sys

sys.setrecursionlimit(10**6)  # 再帰の深さ上限を変更（初期値＝1000)

"""
DFS（深さ優先探索の基本）
計算量：O(N＋M）

＊到達可能性・連結性は求められる＝始点から到達できるかどうか
＊最小移動回数は求められない

始点から行き止まりになるまで順に探索していく
N = 頂点の数 M = 辺の本数 S = 始点
"""

N, M, S = map(int, input().split())
G = [[] for _ in range(N)]  # 隣接リストを作成（無向グラフを作成）
visited_ = [False] * N  # 頂点を訪問済みかどうかを管理する配列

# 無向グラフの隣接リストを作成
for _ in range(M):
    v, u = map(int, input().split())
    G[v].append(u)
    G[u].append(v)


# DFS
def dfs_(s):
    """
    未訪問の頂点がなくなるまで探索を繰り返す

    Args: v 今見ている頂点の番号

    Returns: dfs
    """
    visited_[s] = True
    # 隣接頂点のチェック
    for v in G[s]:
        if not visited[v]:
            dfs_(v)


dfs_(S)


"""
C問題_
"""


N, M = map(int, input().split())
g = [[] for _ in range(N)]
visited_ = [False] * N

# 隣接リストを作成
for _ in range(M):
    v, u = map(int, input().split())
    v -= 1
    u -= 1
    g[v].append(u)
    g[u].append(v)

# 辺の数はN-1
if M != N - 1:
    print("No")
    exit()


# 連結性をチェック
# 全ての頂点が訪問済みになるまで繰り返す
def dfs2(s):
    visited_[s] = True
    for j in g[s]:
        if not visited_[j]:
            dfs2(j)


dfs2(0)
# 全頂点に到達していなければパスグラフではない（連結性がない為）
if not all(visited_):
    print("No")
    exit()

deg1 = sum(1 for i in range(N) if len(g[i]) == 1)
deg2 = sum(1 for i in range(N) if len(g[i]) == 2)

if deg1 == 2 and deg1 + deg2 == N:
    print("Yes")
else:
    print("No")


"""
深さ優先探索（MLE）
メモリ超過エラー

構文自体は合っている
"""

import sys

sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
S = [input() for _ in range(H)]
visited = [[False] * W for _ in range(H)]

si, sj = 0, 0
gi, gj = 0, 0
# 始点と終点の座標を設定
for i in range(H):
    for j in range(W):
        if S[i][j] == "s":
            si, sj = i, j
        if S[i][j] == "g":
            gi, gj = i, j
    if si != 0 and gi != 0:
        break


def dfs(j, i):
    visited[j][i] = True
    # 上下左右のマスを確認
    for dy, dx in ((j - 1, i), (j + 1, i), (j, i - 1), (j, i + 1)):
        if not (0 <= dy < H and 0 <= dx < W):
            continue
        if S[j][i] == "#":
            continue
        if not visited[dy][dx]:
            dfs(dy, dx)


# 始点から呼び出す
dfs(si, sj)

print("Yes" if visited[gi][gj] else "No")


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