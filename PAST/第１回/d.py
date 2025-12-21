
from collections import Counter
N=int(input())
A=list(range(1,N+1))
B=[int(input()) for _ in range(N)]

c=set(A)-set(B)
if len(c)==0:
  print("Correct")
  exit()

y,mx=c,0
x=0
cnt=Counter(B)
for k,v in cnt.items():
  if mx<v:
    mx=v
    x=k
print(x, *y)