"""
C問題
難易度1D

(https://atcoder.jp/contests/abc440/tasks/abc440_c)

"""

t = int(input())

# アルゴリズムの改善：O(N＋W）
for _ in range(t):
  n,w = map(int, input().split())
  c = list(map(int, input().split()))

  # 周期性
  period = 2*w

  cost_sum = [0] * period
  # i（ます）を固定した時にどのxでi（マス）が黒くなるか？
  for i in range(n):
    # 各マスiをi % 2wでグループ化
    # 黒くなるのはwの連続区間
    cost_sum[i % period] += c[i]

  # 円環を直線にするため配列の長さを2倍で設定
  arr = cost_sum + cost_sum

  # xを全探索（固定）せず区間和の最小値問題へ変換している
  # 長さ w の区間和の最小値
  cur = sum(arr[:w])
  ans = cur

  for i in range(w, w + period):
    cur += arr[i]
    cur -= arr[i - w]
    ans = min(ans, cur)

  print(ans)
    
