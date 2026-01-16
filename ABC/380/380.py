"""
A問題_123233 
122333 = 14になる時だけ（最終的な求めたい結果）
"""

N = list(input())
# 並べ替え
N = sorted(N)
print("Yes" if "".join(N) == "122333" else "No")

# 別解
N = list(map(int, input()))
print("Yes" if sum(N) == 14 else "No")



"""
B問題_Hurdle Parsing・・・解けた
難易度27
"""

s = input().split("|")
lst = [len(s_i) for s_i in s if s_i != '']
print(*lst)