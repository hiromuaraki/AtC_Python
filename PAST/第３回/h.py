N,L = map(int, input().split())
X = list(map(int, input().split()))
T1, T2, T3 = map(int, input().split())
H = [False] * (L + 1)

# ハードルがある場所にTrue
for x in X:
  H[x] = True

