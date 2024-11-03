# Created by Nikolay Pakhomov 03.11.2024
def get_evidence_list(n, a, m, k, x):
    result = ""
    return result


n_list = []
a_list = []
m_list = []
k_list = []
x_list = []
result_list = []
with open('input_test.txt') as f:
    test_n = int(f.readline().strip())
    for ii in range(test_n):
        f.readline()
        nn = int(f.readline().strip())
        aa = list(map(int, f.readline().split()))
        mm, kk = map(int, f.readline().split())
        xx = list(map(int, f.readline().split()))
        n_list.append(nn)
        a_list.append(aa)
        m_list.append(mm)
        k_list.append(kk)
        x_list.append(xx)

with open('output_test.txt') as f:
    for ii in range(test_n):
        result_list.append(f.readline().strip())

for ii in range(test_n):
    res = get_evidence_list(n_list[ii], a_list[ii], m_list[ii], k_list[ii], x_list[ii])
    res_str = res.strip()
    print(f"Result: {res_str}, Answer: {result_list[ii]}, Right: {res_str == result_list[ii]}")
