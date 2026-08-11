"""
アナグラムになる確率
(https://algo-method.com/tasks/869)

N個の文字列から2つの相違なる文字列を選ぶ
nC2 = N(N - 1) / 2

同じ代表系を持つ文字列が何個あるか
"""

from collections import Counter

N = int(input())
lst = input().split()
S = []
for s_i in lst:
    S.append("".join(sorted(s_i)))

counter = Counter(S) # 同じ文字列をグループ化

count = 0 # アナグラムになるペア数
# 異なる文字列から相違なる文字列を2つ選ぶ kC2
for k in counter.values():
    count += k * (k - 1) // 2

# 総パターン数 nC2
total = N * (N - 1) // 2 

print(f"{count / total :.13f}")


