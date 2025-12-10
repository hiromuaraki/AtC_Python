"""
A = {1,2,3,5}
B = {1,2,3,4,6}

和集合(+)・・・集合A、集合Bの内少なくとも片方に含まれる要素
A | B
|A ∪ B| = {1,2,3,4,5,6}

差集合(-)・・・集合同士の差を知りたいときに使う
A - B = {5}
B - A = {4, 6}

積集合（＊）・・・・集合同士の共通している要素（共通項）
A & B 
|A ∩ B| = {1,2,3}

対称差（^）・・・・共通部分以外の要素

A^B
|−−−−−|
|A ∩ B| = {5,4,6}

"""


"""
書かれた数の個数（１）

集合Sの中に含まれるXの倍数の個数を求める
N/X（整数除算）で分かる
"""

N,X = map(int, input().split())
print(N // X)

"""
書かれた数の個数 (2)
「条件に重なりがある場合の個数をどう整理するか」

|A ∩ B| = N // lcm(X,Y)
"""

N,X,Y = map(int, input().split())
def gcd(x, y):
    if y == 0: return x
    return gcd(y, x % y)

print(N // (X*Y//gcd(X, Y)))

"""
含まれない数・・・差集合
集合Bに含まれない数は？

集合Aー集合Bの差集合で求められる

sep="\n"で改行ありで出力
"""

N,M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(*sorted(A - B), sep="\n")


"""
書かれた数の個数（３）

A U B = 集合AとBの和集合（A,Bの内、少なくとも片方が含まれる）
集合C＝AにもB２も含まれない数
A｜B
集合S＝N
C＝ N - len(A | B)
"""

N,X,Y = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(N - len(A | B))


"""
書かれた数の個数（４）
ドモルガンの法則
３の倍数でも５の倍数でも割れない数の個数

xの倍数の個数＝N//x

x = 3の倍数の個数＝ N // 3
y = 5の倍数の個数＝ N // 5
z = Nの中の3と5で割れる倍数＝最小公倍数 3 * 5 = 15（集合X、Yの共通部分）

N（全体） - (x+y-z)
"""

N = int(input())
x = N // 3
y = N // 5
z = N // 15
print()


"""
問題007_Number of Multiples 1 ・・・解けた
難しい

和集合＋数の性質

集合の和集合
重複カウントの排除（包除原理）
倍数の性質（LCM）

倍数の性質を使う
N // x = Xの倍数の個数
N // y = yの倍数の個数

x,yの重複する部分を引く必要がある
x,yのダブルカウントする部分＝共通部分＝x,yの最小公倍数
z = N // lcm(x, y) = x,yの共通部分の個数

X の倍数の数 → N // X
Y の倍数の数 → N // Y
共通部分（LCM の倍数） → N // math.lcm(X, Y)
包除原理で x+y−z

最終的な答え
x + y - z
"""

# 数学的解法
import math
N,X,Y = map(int, input().split())
x = N // X
y = N // Y
z = N // math.lcm(X, Y)
print(x + y - z)


# forで愚直 O(N)
ans = 0 
for i in range(1, N + 1):
    if i % X == 0 or i % Y == 0:
        ans += 1
print(ans)

"""
A問題_033_隠れた言葉・・・解けた
難易度65

部分文字列の個数

全部でいくつ部分文字列があるか数え上げる＝部分文字列の総数を求める
N(N + 1)//2

"""

N = int(input())
print(N * (N + 1)//2)


"""
A問題_Distinct Strings
数え上げの問題＋場合分け
"""

S = set(input())
if len(S) == 3: print(6)
elif len(S) == 2: print(3)
else: print(1)