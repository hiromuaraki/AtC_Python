n = int(input())
s = input()

for i in range(n):
  for j in range(i + 1, n):
    for k in range(j + 1, n):
      if s[i] + s[j] + s[k] == "IOI":
        print("Yes")
        exit()
print("No")