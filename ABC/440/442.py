"""
A問題_Count.
"""

s = input()
print(s.count("i") + s.count("j"))


"""
B問題_Music Player
"""


q = int(input())
volume = 0
is_player = False
for _ in range(q):
  a = int(input())
  if a == 1:
    volume += 1
  elif a == 2 and volume > 0:
    volume -= 1
  elif a == 3:
    is_player ^= True
  
  if volume >= 3 and is_player:
     print("Yes")
  else:
    print("No")


"""
C問題_Peer Review
(https://atcoder.jp/contests/abc442/tasks/abc442_c)
4Q
数え上げ問題

研究者iと利害関係がない研究者の中から3人選ぶ方法は何通り？

deg[i] = 研究者 i の利害関係の人数（グラフの次数）
kC3通り = k(k - 1)(k - 2) // 3! = k(k - 1)(k - 2) // 6
k人から3人選ぶ組合せ数


次数（頂点iが何本の辺と繋がっているか）

「頂点i と直接つながっていない頂点から3つ選ぶ方法の数」

3つ選ぶ：kC3 = k * (k - 1)(k - 2) // 3!(6)
ペア：kC2 = k * (k - 1) // 2!(2)
"""

n,m = map(int, input().split())
deg = [0] * n  # 各研究者の利害関係人数を数える配列

for _ in range(m):
  a,b = map(int, input().split())
  a -= 1; b -= 1
  deg[a] += 1
  deg[b] += 1

# 組合せ C(k, 3)
# 各頂点 i について、「i と“つながっていない頂点”から 3 個選ぶ組み合わせ数」を計算している
# n - 1：自分自身を除いた他の頂点数 そこからiと繋がっている頂点を引く
for i in range(n):
  k = n - 1 - deg[i]
  print(k * (k- 1) * (k - 2) // 6)

# k = 7
# kC2通り：kC2 = k * (k - 1) // 2!(2)＝2重ループの回数
for k in range(1,7):
    cnt = 0
    for a in range(k):
        for b in range(a+1, k):
            cnt += 1
    print(k, cnt, k*(k-1)//2)


print("--------------------------------")
# kC3通り：kC3 = k * (k - 1)(k - 2) // 3!(6)＝3重ループの回数
for k in range(1,7):
    cnt = 0
    for a in range(k):
      for b in range(a+1, k):
        for c in range(b+1, k):
          cnt += 1
    print(k, cnt, k*(k - 1)*(k - 2) // 6)