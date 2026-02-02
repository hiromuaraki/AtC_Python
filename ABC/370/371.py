"""
A問題_Jiro
6Q
少し頭使う
(https://atcoder.jp/contests/abc371/tasks/abc371_a)

場合分け
< < < ・・・ B
> > > ・・・ B
< > > ・・・ A
> < < ・・・ A
< < > ・・・ C
> > < ・・・ C
"""

ab,ac,bc = input().split()
if ab != ac: print("A")
elif ab == ac == bc: print("B")
else: print("C")


"""
B問題_Taro
"""

n,m = map(int, input().split())
child = [0] * n
for _ in range(m):
  a,b = input().split()
  a = int(a) - 1
  if b == "M" and child[a] == 0:
    child[a] += 1
    print("Yes")
  else:
    print("No")