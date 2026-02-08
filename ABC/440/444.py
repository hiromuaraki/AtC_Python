"""
A問題_RepDigit
"""

print("Yes" if len(set(input())) == 1 else "No")

"""
B問題_Digit Sum
(https://atcoder.jp/contests/abc444/tasks/abc444_b)
"""

n,k = map(int, input().split())
count = 0
for i in range(1, n + 1):
  total = sum(list(map(int, str(i))))
  if total == k:
    count += 1
print(count)

"""
C問題_AtCoder Riko
(https://atcoder.jp/contests/abc444/tasks/abc444_c)
難しい 候補を仮定して検証する問題

じゃがりこは
・割れなくてもいい
・割れてもいい
・割れる本数は明示されていない


n = シェイクした後のじゃがりこの本数
a = シェイクした後の結果できた長さ

以下の条件を満たす長さL：
・長さがLである１本のじゃがりこ
・長さの和がLであるような２本のじゃがりこ（割れた）

割れていない：L = max(a)
割れている：L = max(a) + min(a)


| あなたの理解         | 実際     |
| -------------- | ------ |
| 割れている／割れていない   | ✅ 完全一致 |
| max(a) は割れていない | ✅ 正しい  |
| max+min は割れている | ✅ 正しい  |
| 相方が必要          | ✅ 正しい  |
| その相方が L-x      | ✅ 正しい  |

"""

from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

# L の候補は max(A) と max(A) + min(A)
candidates = set()
candidates.add(a[-1])
if n >= 2:
    candidates.add(a[-1] + a[0])

# 条件を満たす長さLが作れるかを判定
def can_make(L: int, a: list) -> bool:
    cnt = Counter(a)

    # 割れていない L はそのままOK
    if L in cnt:
        del cnt[L]

    for x in list(cnt.keys()):
        if cnt[x] == 0:
            continue
        y = L - x
        if y not in cnt:
            return False
        if x == y:
            # x + x = L の場合は偶数本必要
            if cnt[x] % 2 != 0:
                return False
            cnt[x] = 0
        else:
            if cnt[x] != cnt[y]:
                return False
            cnt[x] = 0
            cnt[y] = 0
    return True

ans = []
# じゃがりこの候補の長さLを全列挙
for L in sorted(candidates):
  if can_make(L, a):
      ans.append(L)
print(*ans)