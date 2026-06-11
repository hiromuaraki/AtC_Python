"""
各桁の和 (1)
(https://algo-method.com/tasks/2927V4xE)

「N以下の数を1桁ずつ生成しながら、
桁和%Aの余りだけを状態として持って数え上げる」

1 ≦ N ≦ 10^18
桁和 % A == 0の数が欲しい
桁数に注目
例）N＝31
2桁の整数、0〜3が先頭に来る

先頭が3未満ならNより小さいことが確定
先頭が3の場合、N以上か、N未満かの２択あり得る

・今まで決めた 桁和 % Aした余り
・今まで作った桁の先頭がN以上か、完全一致しているかのフラグ（0, 1）

0：今まで作った数がNと完全一致している
1：N未満が確定しているか

dp[i][smaller][r]
[[0,0,0,0,0], [0,0,0,0,0]]
"""

N,A = map(int, input().split())
S = str(N)
L = len(S)

dp = [[[0] * A for _ in range(2)] for _ in range(L + 1)] # Lも含む
dp[0][0][0] = 1 # まだ1桁も決めていない状態。Nと一致状態が1通りのため1

# N以下の左から1桁ずつ作りながら
# N未満確定か、桁和％Aの余りを管理
for i in range(L):
    d = int(S[i])
    
    for smaller in range(2):    
        for r in range(A):
            # 今の状態に何通り到達できるか
            cur = dp[i][smaller][r]
            
            if cur == 0:
                continue
            
            # 次の桁に置ける数字
            mx_digit = (9 if smaller else d)

            for digit in range(mx_digit + 1):
                # smaller更新
                next_smaller = smaller

                if smaller == 0 and digit < d:
                    next_smaller = 1

                # 桁の余り更新
                next_r = (r + digit) % A
                # 今の状態からdigitを置いた結果の状態へ通り数を加算
                dp[i + 1][next_smaller][next_r] += cur
# Nと完全一致の通り数（桁和％A=0）＋N未満の通り数（桁和％A＝０）
print(dp[L][0][0] + dp[L][1][0] - 1)
            

