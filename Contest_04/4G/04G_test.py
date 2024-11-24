# Created by Nikolay Pakhomov 21.11.2024
def calculate_combinations(n, mod, edges):
    result = 0
    return result


n_list = []
m_list = []
k_list = []
result_list = []
a_b_list = []
test_n = 10
for i in range(2, test_n + 2):
    with open(f"input{i}.txt") as f:
        amount, m, k = map(int, f.readline().split())
        n_list.append(amount)
        m_list.append(m)
        k_list.append(k)
        a_b = []
        for m_i in range(m):
            first, second = map(int, f.readline().split())
            a_b.append((first, second))
        a_b_list.append(a_b)

    with open(f"output{i}.txt") as f:
        result_list.append(int(f.readline().strip()))

for ii in range(test_n):
    ans = calculate_combinations(n_list[ii], k_list[ii], a_b_list[ii])
    print(f"Result: {ans}, Answer: {result_list[ii]}, Right: {ans == result_list[ii]}")
