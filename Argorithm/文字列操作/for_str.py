"""
A問題_11/22string・・・・自力AC
難易度31

11/22stringの条件
・1文字目からN+1/2-1までが”１”
・N+1/2（真ん中）が”／”
・N+1/2+1以降が”２”

方針
Tのi番目が”１”の出現する範囲かをi番目がN＋1/2-1未満かで切り分ける
"""

N=int(input())
T=input()
ans=""
for i in range(N):
    if i<((N+1)//2-1) and T[i]=="1":
        ans+="1"
    else:
        if i==N//2:
            ans+="/"
        else:
            ans+="2"

if T==ans:
    print("Yes")
else:
    print("No")


"""
B問題_Echo・・・解けた
難易度49

同じ部分文字列が2度繰り返されているか
"""

N = int(input())
S = input()
T = S[:(len(S)//2)]
print("Yes" if S == T*2 else "No")


"""
B問題_430_FourHidden・・・ギリ解けた
難易度79

部分文字列の判定と走査
"""


T, U = input(), input()
ok = False

# iは開始位置（ループごとに文字が1つずつずれる）
for i in range(len(T) - len(U) + 1): 
  ok = True
  for j in range(len(U)):
    if T[i + j] != "?" and T[i + j] != U[j]:
      ok = False
      break
  if ok:
    print("Yes")
    exit()
print("No")