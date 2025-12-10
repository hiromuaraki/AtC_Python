"""
問題157_Bingo
"""

A=[list(map(int, input().split())) for _ in range(3)]
N=int(input())
M=[[False]*N for _ in range(3)]

# カードが含まれているか確認
for _ in range(N):
  b=int(input())
  for i in range(3):
    for j in range(3):
      if b==A[i][j]:
        M[i][j]=True

bingo=False

for i in range(3):
  if M[i][0] and M[i][1] and M[i][2]:
    bingo=True


for i in range(3):
  if M[0][i] and M[1][i] and M[2][i]:
    bingo=True

if M[0][0] and M[1][1] and M[2][2]:
  bingo=True

if M[0][2] and M[1][1] and M[2][0]:
  bingo=True


if bingo:
  print("Yes")
else:
  print("No")

"""
山崩し・・・自力AC
難しい
"""

N=int(input())
T=[list(input()) for _ in range(N)]

for i in range(N-2, -1, -1):
  for j in range(1, 2*N-1):
    if T[i][j]=="#" and (T[i+1][j-1]=="X" or T[i+1][j]=="X" or T[i+1][j+1]=="X"):
      # 左下 真下 右下
        T[i][j]="X"
  
for i in range(N):
  print("".join(T[i]))


"""
地図の切り取り・・・グリッド
"""

H,W,x,y=map(int, input().split())
S=[list(input()) for _ in range(H)]
x-=1
y-=1
for i in range(3):
    for j in range(3):
        print(S[x+i][y+j], end="")
    print()



"""
縦横十時・・・グリッド
"""

H,W=map(int, input().split())
S=[list(input()) for _ in range(H)]
p,q=map(int, input().split())
c=set()

for i in range(W):
    if S[p][i]=="#":
        c.add((p,i))

for j in range(H):
    if S[j][q]=="#":
        c.add((j,q))
print(len(c))




"""
マインスイーパー・・・グリッド
"""

H,W=map(int, input().split())
S=[list(input()) for _ in range(H)]
Q=int(input())

for _ in range(Q):
    count=0
    x,y=map(int, input().split())

    for _ in range(1):
        if y != 0 and S[x][y-1]=="#":count+=1 # 左
        if y != W-1 and S[x][y+1]=="#":count+=1 # 右
        if x != 0 and S[x-1][y]=="#":count+=1 # 上
        if x != H-1 and S[x+1][y]=="#":count+=1 # 下
    print(count)


"""
ロボットの移動・・・グリッド
(sx, sy)=(行、列)
難しい
"""

H,W,sx,sy=map(int, input().split())
S=[input() for _ in range(H)]
N=int(input())
T=input()

for move in T:
    if move=="L" and sy>0 and S[sx][sy-1]==".":sy-=1
    if move=="R" and sy+1<W and S[sx][sy+1]==".":sy+=1
    if move=="U" and sx>0 and S[sx-1][sy]==".":sx-=1
    if move=="D" and sx+1<H and S[sx+1][sy]==".":sx+=1

print(sx,sy)