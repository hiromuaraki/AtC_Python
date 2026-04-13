"""
数を選ぶ (1)
(https://algo-method.com/tasks/428)

組合せを列挙する問題
★a0数を使う／a0使わないの全探索
再帰で木を辿っている

f(n,l,r)=f(n−1,l,r)+f(n,l+1,r)
"""

def func(n: int, l: int, r: int) -> list:
  if l > r: return []
  if n == 0: return [[]]
  ans = []
  # n-1番目の要素としてlを選んだ場合
  for x in func(n - 1, l, r):
    to = [l]
    to.extend(x)
    ans.append(to)
  # lを選ばなかった場合
  ans.extend(func(n, l + 1, r))
  return ans


N,L,R = map(int, input().split())
for x in func(N, L, R):
  print(*x)


# DFS解法
def dfs(l, path):
  if len(path) == N:
    print(*path)
    return
  for i in range(l, R+1):
    path.append(i)
    dfs(i, path)
    path.pop()

N, L, R = map(int, input().split())
dfs(L, [])