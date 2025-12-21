"""
A問題_Leyland Number
"""

A,B = map(int, input().split())
print(A**B + B**A)

"""
B問題_Longest Palindrome・・・解けない（もう少し）
難易度84
"""

S = input()
N = len(S)

ans = 1
for i in range(N):
  for j in range(i + 1, N + 1):
    s = S[i:j]
    if s == s[::-1]:
        ans = max(ans, len(s))
print(ans)
