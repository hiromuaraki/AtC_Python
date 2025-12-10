import itertools

"""
問題B_425_findPermutatons_順列全探索・・・自力AC
難易度82
難しい

順列全探索＝N!通り試す

入力：-1,1 ≦ N与えられる
1..NまでのPを並べ替えた数列とAが一致するかを判定する

A＝
・-1＝何でもいい
・-1以外＝固定
・Aの中で重複していたらその時点で条件は成立しない

P＝重複してはいけない かつ 1以外の位置は固定

方針：
Aの要素の中に-1以外の要素が重複しているかを調べる。重複していたらその時点でNo

"""

N = int(input())
A = list(map(int, input().split()))

# 公式解法
for p in itertools.permutations(range(1, N+1)):
  ok = True
  for i in range(N):
    ok &= A[i] == -1 or p[i] == A[i]
  if ok:
    print("Yes")
    print(*p)
    exit()
else:
  print("No")



"""
C問題114_753数
3、5、7の全列挙
"""


N = int(input())
digits = ["3", "5", "7"]
L = len(str(N))

ans = 0
for k in range(3, L + 1):
  for p in itertools.product(digits, repeat=3):
    s = "".join(p)
    if "3" in s and "5" in s and "7" in s:
      if int(s) <= N:
        ans += 1
print(ans)