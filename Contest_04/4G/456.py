def f(a, n, p):
    if n:
        for i in range(n + 1, 0, -1):
            if i <= p:
                f(a + [i], n - i, i)
    else:
        print(*a, sep=' + ')


# n на k слагаемых
def find_options(n, k):
    a = []
    j = n
    if n:
        while j > 0:
            find_options(n - 1, k)
            j -= 1
        pass
    else:
        return a


n = 5
k = 4
f([], n, n)
