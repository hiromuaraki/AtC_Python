"""
A問題_Octave

シフト演算でベキ乗計算
2^y
"""

x,y = map(int, input().split())
print(x << y)


"""
B問題_Trifecta
(https://atcoder.jp/contests/abc440/tasks/abc440_b)
"""

n = int(input())
t = list(map(int, input().split()))
lst = sorted(t)
dic = {v : i + 1  for i, v in enumerate(t)}
for i in range(3):
  print(dic[lst[i]], end=" ")


"""
C問題_Striped Horse
(https://atcoder.jp/contests/abc440/tasks/abc440_c)

x によって「黒くなる位置のパターン」が決まり、その中から最小コストのパターンを選ぶ問題
＝円環配列 × 幅 W の区間和の最小値問題

周期性（円環）＝2w

正整数xを自由に選び、1 <= 1 <= nを満たす整数iのうち、 
(i + x) % 2w < wを満たす全てのマスに対してマスiを黒く塗る。

この手順を行う行うためのコストの合計の最長値を求める

制約：
t <= 2*10^5
1 <= n <= 2*10^5
1 <= w <= 2*10^5
1 <= c <= 10^9

円環問題は、配列を長さを2倍にする
全探索 → 集約 → 区間和への変換
円環 → 配列2倍テク
"""

t = int(input())
INF = 10**18

# アルゴリズムの改善：O(N＋W）
for _ in range(t):
  n,w = map(int, input().split())
  c = list(map(int, input().split()))

  # 周期性
  period = 2*w

  cost_sum = [0] * (period + 1)
  # i（マス）を固定した時にどのxでi（マス）が黒くなるか？
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


# 愚直：O(WN）全探索＝4*10^10
# 全探索：xを固定して全iを見る
for _ in range(t):
  n,w = map(int, input().split())
  c = list(map(int, input().split()))
  period = 2*w
  sum_cost = INF
  
  # コスト計算：(w,i)組の全てのマスを走査
  # ボトルネック：xごとにnを全走査している部分
  # xごとに全iを見て条件判定しコストを足す処理を全(x, i)組に対して行うから遅い
  for x in range(1, period+1):
    cost = 0
    for i in range(n):
      # 長さ 2W の周期の中で、連続する W 個の区間に入っている
      # index だけを選ぶ
      if (i + x) % period < w:
        cost += c[i]
    sum_cost = min(sum_cost, cost)
  print(sum_cost)
