"""
A問題_Robot Balance
"""

H,B = map(int, input().split())
print(max(0, H - B))

"""
B問題_Robot Weight・・・解けた
難易度
"""

X = int(input())
N = int(input())
W = list(map(int, input().split()))
Q = int(input())

lst = [0] * N
ans = 0
for i in range(Q):
  P = int(input())
  P -= 1
  lst[P] ^= 1
  if lst[P]:
    X += W[P]
  else:
    X -= W[P]
  print(X)

"""
C問題_RobotFactory・・・解けない
ソート＋貪欲法（または二分探索法）

軽い頭パーツを軽い体パーツに割り当てる選択を繰り返す方針
"""

N,M,K = map(int, input().split())
H = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))

i,j,count = 0,0,0
while i < N and j < M:
  if H[i] <= B[j]:
    count += 1 # ロボット１体作る
    i += 1 # 次の頭パーツへ移動
    j += 1 # 次の体パーツへ移動
  else:
    j += 1 # H[i] > B[i]の為次の体パーツへ移動
  
  if count == K:
    print("Yes")
    exit()
print("No")