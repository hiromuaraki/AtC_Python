from collections import Counter

"""
バブルソート
計算量：O(N^2)

隣同士の並べ替え（昇順）

隣接する２つの要素の大きさが逆転していたら並べ替える
並べ替えの過程を出力
"""

N=int(input())
A=list(map(int, input().split()))

for _ in range(N):
    is_swap=False
    for j in range(N-1):
        if A[j+1] < A[j]:
            A[j],A[j+1]=A[j+1],A[j]
            is_swap=True
    if is_swap:
        print(*A)
    else:
        break

"""
選択ソート・・・理解不足

計算量：O(N^2)

配列から最小の要素を取り出すことを繰り返す
最小の要素の位置
検索範囲をk+1ずつ減らしていく

5

2 1 3 4 1 = 1

k=0
1 2 3 4 1

k=1
2 3 4 1 = 1

1 1 3 4 2
"""

N=int(input())
A=list(map(int, input().split()))

for k in range(N-1):
  min_idx = A[k:].index(min(A[k:])) + k
  A[k],A[min_idx] = A[min_idx], A[k]
  print(*A)



"""
挿入ソート
計算量：O(N^2)

昇順にソートされた配列の適切な位置に要素を挿入すると、挿入後の配列もまた昇順にソートされている。
"""


N=int(input())
A=list(map(int, input().split()))

for k in range(1, N):
    pos=k
    while pos!=0 and A[pos-1] > A[pos]:
        A[pos-1],A[pos]=A[pos],A[pos-1]
        pos-=1
    print(*A)


"""
バケットソート・・・難しい
計算量：O(N+Akind)？

＝累積和を使った座席割り当て

座る場所の位置を累積和で事前に計算
・各数字の登場回数（頻度分布）
・各数字の総数


要素同士の値を比較しないソートである
要素を取り出すためのN個分のバケツを用意

5
2 1 3 4 1

1:2
2:1
3:1
4:1

各要素数を配列に記録
[0,2,1,1,1]
"""

N=int(input())
A=list(map(int, input().split()))
X=N+1

num=[0]*X
# 各要素を数える（頻度分布）
# 数字xが何回出てくるか
for a in A:
    num[a]+=1

# 並べる位置を決める（累積和）
# 「0 〜 x までに出てきた数字の総数」
# 各数字が「並べ替えたリストでどこから始まるか」を計算
# acc[x] = 「数字 x までに、全部で何個の数字が出てきたか」
# 数字の置き場所を前もって決める
acc=[0]*X
for x in range(N):
    if x==0: acc[x]=num[x]
    else:acc[x]=acc[x-1]+num[x]

B=[0]*N
for a in A:
    acc[a]-=1
    B[acc[a]]=a

print(*B)

"""
中央値
"""

N=int(input())
A=list(map(int, input().split()))
A.sort()
if N%2!=0:
    print(A[N//2])
else:
    n=sum(A[(N//2)-1:(N//2)+1])
    print(n/2)

"""
X番目に小さい数
"""

N,M=map(int, input().split())
A=list(map(int, input().split()))
X=list(map(int, input().split()))
A.sort()

for x in X:
    print(A[x])

"""
総和の最大値
"""

N,K=map(int, input().split())
A=list(map(int, input().split()))
print(sum(sorted(A, reverse=True)[:K]))


"""
差の最小値・・・難しい（要復習）
計算量：O(N log N)

連続 K 個を見れば「その K 個の最大−最小」が簡単に求まる
最小差＝ソート後の連続 K 個

N-K＋1＝連続してK個を取れる総数（取り方の数）
"""

N,K=map(int, input().split())
A=list(map(int, input().split()))
best=float("inf")
A.sort()
for i in range(N-K+1):
    diff=A[i+K-1]-A[i]
    if diff < best:
        best=diff
print(best)

"""
在庫付き最小コスト購入・・・難しい

安いものから順に買っていく→先に（価格、在庫）のペアを価格で昇順にする
[(2,1),(4,3),(6,5)]
"""

N,K=map(int, input().split())
items=[tuple(map(int, input().split())) for _ in range(N)]
items.sort(key=lambda p: p[0])

need,cost=K,0
for price,stock in items:
    buy=min(stock, need)
    cost+=price*buy
    need -= buy
    
    if need == 0:
        break
print(cost)

"""
文字数の種類
"""

N=int(input())
S=set(input().split())
print(len(S))


"""
文字列に現れない文字
"""

S=set(input())
D=set(chr(ord("a")+i) for i in range(26))
print(len(D-S))


"""
注文
"""

N,M=map(int, input().split())
menu={}
for _ in range(N):
    f_,price=input().split()
    menu[f_]=int(price)
X=input().split()

total=0
for x in X:
    total+=menu[x]
print(total)


"""
最頻文字列

まず出現回数が多い順に並べる
出現回数が同じ場合は、文字列を辞書順で並べる

条件：
1. 出現回数の多い順＝-item[1]
2. 回数が同じ場合は、文字列の辞書順
"""

N=input()
S=input().split()
count=Counter(S)
ans=sorted(
    count.items(),
    key=lambda item: (-item[1], item[0]))
print(ans[0][0])