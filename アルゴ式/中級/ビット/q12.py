"""
オセロ盤の圧縮
(https://algo-method.com/tasks/1260uphP)

👉 << → ビットを移動（位置指定）
👉 & → ビットを残す（マスク）
👉 >> & 1 → 0/1として取り出す
"""
x = list(map(int, input().split()))

for i in range(8):
  row = []
  print(f"\n--- 行 {i} ---")
  print(f"x[i] = {x[i]} ({x[i]:016b})")  # 16ビットで表示

  for j in range(8):
    bit0_pos = 15 - 2*j # 15-2j番目に1を立てている（マスクを作る）1000000000000000（= 32768）j = 0の場合
    bit1_pos = 14 - 2*j # 15-2j番目に1を立てている（マスクを作る）1000000000000000（= 32768）j = 0の場合
    # 👉 マスク作成 → 抜き出し → 判定
    x0 = x[i] & (1 << bit0_pos)
    x1 = x[i] & (1 << bit1_pos)

    print(f"j={j} | 見てるビット: {bit0_pos},{bit1_pos} | x0={x0} x1={x1}")

    if not x0 and not x1:
      row.append(".")
    elif not x0 and x1:
      row.append("o")
    elif x0 and not x1:
      row.append("x")

  print("結果:", "".join(row))



# x = list(map(int, input().split()))

# for i in range(8):
#   row = []
#   for j in range(8):
#     v = (x[i] >> (14 - 2*j)) & 3  # 2ビットまとめて取得
    
#     if v == 0:
#       row.append(".")
#     elif v == 1:
#       row.append("o")
#     else:  # v == 2
#       row.append("x")
  
#   print("".join(row))