"""
数列の部分和
(https://algo-method.com/tasks/1130VGA4)
"""

n,x = map(int, input().split())
a = list(map(int, input().split()))
print(sum(a[i] for i in range(n) if x & 1 << i))
