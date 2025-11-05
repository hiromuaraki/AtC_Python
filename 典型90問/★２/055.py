"""
【全探索・・・定数倍を見積もる】

nC5通り試す
各Aを％Pし先に値を縮小→処理が高速になる
"""
N,P,Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N): # 0
  for j in range(i + 1, N): # 1
    for k in range(j + 1, N): # 2
      for l in range(k + 1, N): # 3
        for m in range(l + 1, N): # 4
            if (A[i]%P * A[j]%P * A[k]%P * A[l]%P * A[m]%P) == Q:
              ans += 1
print(ans)