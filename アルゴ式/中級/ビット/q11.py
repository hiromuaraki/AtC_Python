"""
電光掲示板の切り替え
(https://algo-method.com/tasks/1698jGFr)
"""

n,m = map(int, input().split())
bit = [
  "1110111", "0100100", "1011101", "1101101", "0101110",
	"1101011", "1111011", "0100111", "1111111", "1101111",
]
a = bit[n][::-1]
b = bit[m][::-1]
print(sum(1 << i for i in range(6, -1, -1) if (int(a[i]) != int(b[i]))))

# 別解
mask_a = int(bit[n], 2)
mask_b = int(bit[m], 2)
print(mask_a ^ mask_b)
