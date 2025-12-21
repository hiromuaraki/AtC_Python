"""
整数に変換できる場合：整数型へ型変換後2*２
整数に変換できない場合：errorを出力
"""
S=input()
print(int(S)*2 if S.isdigit() else "error")