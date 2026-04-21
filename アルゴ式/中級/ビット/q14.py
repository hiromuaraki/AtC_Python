"""
サブネットマスク
(https://algo-method.com/tasks/17028BFG)
"""

sub = [255, 255, 252, 0]
ip = [172, 60, 123, 0]
s = []
for i in range(4):
  s.append(str(sub[i] & ip[i]))
print(".".join(s))
