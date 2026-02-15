"""
Ex. ハッシュテーブル
(https://algo-method.com/tasks/878)
"""

q = int(input())
s = set()

# s setは内部的にハッシュテーブル
for _ in range(q):
  query, t = input().split()
  query = int(query) 
  if query == 0:
    s.add(t)
  elif query == 1:
    s.remove(t)
  else:
    print("Yes" if t in s else "No")



# 別解（自作ハッシュテーブルの管理）
BASE = 30
MOD = 10**6
hash_table = [[] for _ in range(MOD)]
def hash_word(word):
  k = 0
  for w in word:
    k = (k * BASE + (ord(w) - ord('a') + 1)) % MOD
  return k

for _ in range(q):
  query, t = input().split()
  query = int(query)
  k = hash_word(t)
  bucket = hash_table[k]
  if query == 0:
    if t not in bucket:
      bucket.append(t)
  elif query == 1:
    if t in bucket:
      bucket.remove(t)
  else:
    print("Yes" if t in s else "No")