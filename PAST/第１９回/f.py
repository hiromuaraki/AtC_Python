from collections import deque, defaultdict

N = int(input())
X,Y = input().split()
edges = defaultdict(list) # 

for i in range(N): #辞書型リストの作成
  s,t = input().split()
  edges[s].append(t)

print(edges)


