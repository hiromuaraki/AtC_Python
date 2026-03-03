"""
お菓子 (2)
(https://algo-method.com/tasks/364)

3の倍数で割れるか
割れないか
"""

n = int(input())
count = 0
while n > 0:
    count += 1
    if n % 3 == 0: n //= 3
    else: n -= 1
print(count)