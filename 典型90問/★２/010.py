"""
区間の総和

計算しやすい形に整える
事前に前計算しR-L−１ O(1)で求める

"""

N = int(input())
S1 = [0] * (N + 1)
S2 = [0] * (N + 1)
for i in range(N):
  c,p = map(int, input().split())
  if c == 1:
    S1[i + 1] = S1[i] + p
    S2[i + 1] = S2[i]
  else:
    S2[i + 1] = S2[i] + p
    S1[i + 1] = S1[i]

Q = int(input())
for _ in range(Q):
  L,R = map(int, input().split())
  print(S1[R] - S1[L - 1], S2[R] - S2[L - 1])