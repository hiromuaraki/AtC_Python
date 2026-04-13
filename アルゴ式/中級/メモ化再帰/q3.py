"""
フィボナッチ数列
(https://algo-method.com/tasks/425)

メモ化前：
func(4)を計算します。
func(3)を計算します。
func(2)を計算します。
func(1)を計算します。
func(0)を計算します。
func(1)を計算します。
func(2)を計算します。
func(1)を計算します。
func(0)を計算します。

メモ化後：
func(4)を計算します。
func(3)を計算します。
func(2)を計算します。
func(1)を計算します。
func(2)を計算します。
"""

def func(x: int) -> int:
  print(f"func({x})を計算します。")
  if x == 0: return 0
  if x == 1: return 1
  return func(x - 1) + func(x - 2)

n = int(input())
print(func(n))