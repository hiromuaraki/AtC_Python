"""
A問題_028_小石を取るゲーム
難易度104


周期（シミュレーション）または計算（サイクル）
シミュレーション
1周＝Antの1手＋Bugの1手
＝（A＋B）ごとのサイクル

N // (A + B)＝確定サイクル

1周の完全なサイクル＝(A + B)
最後に残るあまり＝r = N % (A + B)


区間判定：
r = 0：最後の袋がちょうど空になる＝Bug
1 <= r <= A:Antのターンで一度に取れる＝Ant
A < r <= A+B:

求めたいのは、
N番目に選ばれるのはAntかBugか？

r = N % (A + B)
r = 0 :最後まで使い切った
r > 0 :最後のサイクルの途中

サイクル（A+B）を1周するとき：

 0〜A：Ant の攻撃区間
 A〜A+B：Bug の攻撃区間

"""

# シミュレーション
N,A,B = map(int, input().split())
count = N
i = 0
while count > 0:
  if i % 2 == 0: count -= A
  else: count -= B

  if i % 2 == 0 and count <= 0:
    print("Ant")
    exit()
  i += 1
print("Bug")

# 数学的解法
N,A,B = map(int, input().split())
r = N % (A + B)
if r == 0: print("Bug")
elif r <= A: print("Ant")
else: print("Bug")