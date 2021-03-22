"""
Find total supply S_n after n iterations starting with
S_0 supplied and B_0 borrowed

c = collateral ratio
S_i = supplied after i iterations
B_i = borrowed after i iterations
S_0 = current supplied
B_0 = current borrowed

borrowed and supplied after n iterations
    B_n = cS_(n-1)
    S_n = S_(n-1) + (cS_(n-1) - B_(n-1))

you can prove using algebra and induction that
    B_n / S_n <= c
    S_n - S_(n-1) = c^(n-1) * (cS_0 - B_0)
    S_n = S_0 + sum (c^i * (cS_0 - B_0)), 0 <= i <= n - 1
        = S_0 + (cS_0 - B_0) * ((1 - c^n) / (1 - c))
    S_n <= S_0 + (cS_0 - B_0) / (1 - c)
"""

c = 0.71 * 10 ** 18
s0 = 10 ** 18
b0 = 0
n = 30

s = s0
b = b0
# S_n = S_0 + sum (c^i * (cS_0 - B_0))
s_i = s0
c_i = 10 ** 18
r = (c / 10 ** 18) * s0 - b0

print('i, supplied, borrowed, s_i, borrowed / supplied, supplied - s_i')

for i in range(1, n + 1):
    s_prev = s
    b_prev = b

    b = c * s_prev / 10 ** 18
    s = s_prev + ((c * s_prev / 10 ** 18) - b_prev)

    if i == 1:
        c_i = 1
    else:
        c_i *= c / 10 ** 18

    s_i += r * c_i

    # print(f'{i} ----------------')
    # print(f'supplied: {s}')
    # print(f'borrowed: {b}')
    # print(f'borrowed / supplied: {b / s}')
    # print(f's_i: {s_i}')
    # print(f's_i - supplied: {s_i - s}')

    """
    python lev.py > lev.csv
    """
    print(f'{i}, {s}, {b}, {s_i}, {b/s}, {s - s_i}')


