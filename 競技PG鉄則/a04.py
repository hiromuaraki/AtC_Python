"""
Binary Representation 1
"""

n = int(input())
b = ""
while n > 0:
  b = str(n % 2) + b
  n //= 2
digit = 10 - len(b)
print("0"*digit + b)
