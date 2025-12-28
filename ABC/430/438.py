"""
A問題_First Contest of the Year

難易度6Q（読解が難しい）
(https://atcoder.jp/contests/abc438/tasks/abc438_a)

周期性 or シミュレーション

f - d：年を跨いだ瞬間のズレ
+7：マイナスを防ぐ保険
%7：7日周期に折りたたむ
"""

d, f = map(int, input().split())

# 次の年のコンテスト開催日をシミュレーション
# 7日ごとにコンテストを開催し年を超えた直後の位置を知りたい
while f <= d:
  f += 7
print(f - d)

# 算数
# 7日周期で何日ズレているか
# 1年＝D日経つと周期上ではD日分ずれる,そのズレを7で割った余り
print((f - d + 7) % 7)

"""
B問題_Substring 2
(https://atcoder.jp/contests/abc438/tasks/abc438_b)

部分文字列＋円環（周期）＋全探索
難易度5Q
()
"""

n, m = map(int, input().split())
s = input()
t = input()

ans = 10**5 # O(NM)=100*100=10000=10^4なので10^5=100000で足りる
# 文字列tがsに含まれる部分文字列を探すので
# n-m+1（最後のm文字含めるために+1）通りの開始位置を設定
for i in range(n - m + 1):
  cost = 0 # tが部分文字列sと一致する最小の操作回数
  for j in range(m):
    s_digit = int(s[i + j])
    t_digit = int(t[j])
    # tの数字を+1操作させただけでsの数字に一致させる最小回数を求める（0-9の円環）
    cost += (s_digit - t_digit + 10) % 10
  ans = min(ans, cost)
print(ans)
  

