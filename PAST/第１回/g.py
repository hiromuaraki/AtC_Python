"""
bit全探索・・・まだ理解できない
集合に対する全探索を行う問題
N人を3つのグループに分けたとき、全グループの幸福度の総和が最大になるようにしたい

要素を含む、含まないの2通り＊N-1個
2^N通り試す＝ALL
1<<N = 2^N

計算量：O(4^N)
[0]*(i+1)はダミーデータ、要素数の数調整

"""
N=int(input())
A=[[0]*(i+1)+list(map(int, input().split())) for i in range(N-1)]
# 集合としてあり得るものの個数
ALL=1<<N

happy=[0]*ALL

# nで表現される集合に要素iが含まれるかを判定
def has_bit(n, i):
  return (n & (1 << i) > 0)

# 幸福度の値を前もって計算
for n in range(ALL):
  for i in range(N):
    for j in range(i+1, N):
      if has_bit(n, i) and has_bit(n, j):
        happy[n]+=A[i][j]

ans=-10**100

for n1 in range(ALL):
  for n2 in range(ALL):
    # n1とn2で重複があれば無視する
    if n1&n2 > 0:
      continue
    # 全体集合の中のn3に含まれていない要素を求める
    n3=ALL-1 - (n1|n2)
    ans=max(ans, happy[n1]+happy[n2]+happy[n3])

print(ans)