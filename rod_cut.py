__author__ = 'hp1'

p = {1: 1, 2: 5, 3: 8, 4: 9, 5: 10, 6: 17, 7: 17, 8: 20, 9: 24, 10: 30}


def cut_rod_recursive(p, n):
    if n == 0:
        return 0
    q = -inf
    for i in range(1, n+1):
        q = max(q, p[i]+cut_rod_recursive(p, n-i))
    return q


def cut_rod_memoized(p, n):
    r = np.zeros(shape=(n+1,))
    # r = []
    return cut_rod_memoized_AUX(p, n, r)


def cut_rod_memoized_AUX(p, n, r):
    if r[n] > 0:
        # print(r[n])
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -inf
        for i in range(1, n+1):
            q = max(q, p[i]+cut_rod_memoized_AUX(p, n-i, r))
    r[n] = q
    return q


def cut_rod_bottom_up(p, n):
    r = np.zeros(shape=(n+1,))
    # r = []
    #r[0] = 0
    # r.append(0)
    for j in range(1, n+1):
        q = -inf
        for i in range(1, j+1):
            q = max(q, p[i]+r[j-i])
        r[j] = q
    return r[n]


def cut_rod_bottom_up_extended(p, n):
    # r = []
    r = np.zeros(shape=(n+1,))
    s = np.zeros(shape=(n+1,))
    # s = []
    for j in range(1, n+1):
        q = -inf
        for i in range(1, j+1):
            if q < p[i] + r[j-i]:
                q = p[i]+r[j-i]
                s[j] = i
        r[j] = q
    return r, s


def cut_rod_print_sol(p, n):
    (r, s) = cut_rod_bottom_up_extended(p, n)
    while n > 0:
        print s[n]
        n -= s[n]


def main():
    n = 4
    # print(n)
    revenue = cut_rod_recursive(p, n)
    print(" Revenue using recursive approach is")
    print(revenue)
    revenue_memoized = cut_rod_memoized(p, n)
    print(" Revenue using memoized is ")
    print(revenue_memoized)
    revenue_bottom_up = cut_rod_bottom_up(p, n)
    print(" Revenue using Bottom up is ")
    print(revenue_bottom_up)
    print(" The cuts are ")
    cut_rod_print_sol(p, n)


if __name__ == '__main__':
    from numpy import *
    import numpy as np
    main()
