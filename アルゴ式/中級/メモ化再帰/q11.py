"""
Ex. 昇順数
(https://algo-method.com/tasks/429)

前の桁以上を選ぶ＝前の桁を保持する
num：現在値
last：最後の桁 0〜9(10進数)
L：最小値（開始）
R：最大値（終了）
"""

def dfs(num, last):
  if num > R: return
  if num >= L:
    global ans
    ans += num
  
  for d in range(last, 10):
    dfs(num * 10 + d, d) # 数の構築
  return

L,R = map(int, input().split())
ans = 0

for i in range(1, 10):
  dfs(i, i)
print(ans)