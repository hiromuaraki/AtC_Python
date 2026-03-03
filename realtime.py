# x = int(input())
# a = list(map(int, input().split()))
# values = [50, 10, 5, 1]
# ans = 0
# for i in range(4):
#   use = min(a[i], x // values[i])
#   ans += use
#   x -= values[i] * use
# print(ans)

# n = int(input())
# count = 0
# while n > 0:
#   count += 1
#   if n % 3 == 0: n //= 3
#   else: n -= 1
# print(count)

# n = int(input())
# a = list(map(int, input().split()))
# prev = a[0]
# ans = 0
# for i in range(1, n):
#   if a[i] < prev:
#     ans += prev - a[i]
#   prev = max(prev, a[i])
# print(ans)

# n = int(input())
# a = set(map(int, input().split()))
# ret = 0
# while len(a) > 0:
#   ret += 1
#   min_val = min(a)
#   a = set(a_i for a_i in a if a_i % min_val != 0)
# print(ret)




