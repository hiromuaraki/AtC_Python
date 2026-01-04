n = int(input())
limit = int(n**0.5)
cnt = [0] * (n + 1) # 1回のみ出現する良い整数の件数を管理

for x in range(1, limit + 1):
  for y in range(x + 1, limit + 1):
    sq = x*x + y*y
    if sq > n:
      break
    cnt[sq] += 1

# 出現回数が1件のみを抽出＝良い整数
good = [i for i, v in enumerate(cnt) if v == 1]
print(len(good))
print(*good)