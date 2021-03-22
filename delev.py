"""
Find S_0, amount of supply with 0 leverage, after n iterations starting with

S_n supplied and B_n borrowed
c = collateral ratio
S_n = current supplied
B_n = current borrowed

S_(n-i) = supplied after i iterations
B_(n-i) = borrowed after i iterations
R_(n-i) = Redeemable after i iterations
    = S_(n-i) - B_(n-i) / c
    where B_(n-i) / c = min supply needed to borrow B_(n-i)

For 0 <= k <= n - 1
    S_k = S_(k+1) - R_(k+1)
    B_k = B_(k+1) - R_(k+1)
and
    S_k - B_k = S_(k+1) - B_(k+1)
so
    S_0 - B_0 = S_1 - S_2 = ... = S_n - B_n
S_0 has 0 leverage so B_0 = 0 and we get
    S_0 = S_0 - B_0 = S_n - B_n

------------------------------------------

Find S_(n-k), amount of supply, after k iterations starting with
S_n supplied and B_n borrowed
with algebra and induction you can derive that
R_(n-k) = R_n / c^k
S_(n-k) = S_n - sum R_(n-i), 0 <= i <= k - 1
        = S_n - R_n * ((1 - 1/c^k) / (1 - 1/c))
"""
c = 0.71 * 10 ** 18
s_0 = 10 ** 18
lev = 1 / (1 - (c / 10 ** 18)) * (10 ** 18)
s_n = 0.9999 * (lev / (10 ** 18)) * s_0
b_n = 0.9999 * (c / (10 ** 18)) * s_n
r_n = s_n - b_n / (c / 10 ** 18)
n = 30

s = s_n
b = b_n

print('i, supplied, borrowed, supplied - borrowed, borrowed / supplied, s_i, supplied - s_i')

for i in range(1, n + 1):
    if b == 0:
        break

    r = min(s - b / (c / 10 ** 18), b)
    s = s - r
    b = b - r

    # unleveraged
    u = s - b

    """
    S_(n-k) = S_n - sum R_(n-i), 0 <= i <= k - 1
            = S_n - R_n * ((1 - 1/c^k) / (1 - 1/c))
    """
    s_i = s_n - min(r_n * ((1 - (1 / (c / 10 ** 18) ** i)) / (1 - 1 / (c / 10 ** 18))), b_n)

    # print(f'{i} ----------------')
    # print(f'supplied: {s}')
    # print(f'borrowed: {b}')
    # print(f'borrowed / supplied: {b / s}')
    # print(f's - b: {s - b}')
    # print(f's_i: {s_i}')
    # print(f's - s_i, {s - s_i}')

    """
    python delev.py > delev.csv
    """
    print(f'{i}, {s}, {b}, {s - b}, {b/s}, {s_i}, {s - s_i}')
