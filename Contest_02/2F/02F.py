# Created by Nikolay Pakhomov 27.10.2024
def get_prefix_sum(sequence):
    prefixsum = [0] * (len(sequence) + 1)
    prefixmulti = [0] * (len(sequence) + 1)
    prefixsub = [0] * (len(sequence) + 1)
    for i in range(len(sequence) - 1, -1, -1):
        prefixsum[i] = prefixsum[i + 1] + sequence[i]
        prefixmulti[i] = sequence[i] * prefixsum[i + 1]  # сумма всех правых на a_i
        prefixsub[i] = prefixsub[i + 1] + prefixmulti[i]
    prefixsub.pop(0)
    return prefixsub


def find_number_by_mod(n, a, prefix_sum, mod):
    result = 0
    for i in range(n - 2):
        result += (a[i] * prefix_sum[i]) % mod
    return result


with open("input2.txt") as f:
    nn = int(f.readline().strip())
    al = list(map(int, f.readline().split()))

# Сортировка O(n*log n)
# al.sort()
factor = 1_000_000_007
prefix = get_prefix_sum(al)
ans = find_number_by_mod(nn, al, prefix, factor)
print(ans)
