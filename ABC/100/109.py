"""
B問題_Shiritori
"""
w_lst = []
n = int(input())
for _ in range(n):
  w = input()
  if w in w_lst:
    print("No")
    exit()
  w_lst.append(w)

for i in range(n - 1):
  if w_lst[i][-1] != w_lst[i + 1][0]:
    print("No")
    exit()
print("Yes")
