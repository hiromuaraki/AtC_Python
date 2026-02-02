"""
A問題_1-2-4 Test

ビット演算

8 4 2 1（桁）
a,b10進数を2進数へ変換し桁の総和を足す
"""

a,b = map(int, input().split())
print(a | b)


"""
B問題_Hammer
難しい
(https://atcoder.jp/contests/abc270/tasks/abc270_b)

① 壁が邪魔しない
Y <= 0  または  Y >= X：x

② 壁が邪魔する（0 < Y < X）

②-a ハンマーが壁の手前にある
Z <= Y：|z| + |x - z|

②-b ハンマーが壁の向こう側
Z > Y：-1 

向きをそろえる
  ↓
壁が区間 (0, X) にあるか？
  ↓
あるなら Z が Y より手前か？

・向きを揃えられないか
"""

x,y,z = map(int, input().split())

if y < 0:
  x = -x
  y = -y
  z = -z

# 壁が目の前にない（直接）
if x < y:
  print(abs(x))
# 壁が目の前にある（ハンマー拾えるか９
else:
  if z > y:
    print(-1)
  else:
    print(abs(z) + abs(x - z))