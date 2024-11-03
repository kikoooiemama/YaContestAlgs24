# Created by Nikolay Pakhomov 03.11.2024
def get_evidence_list(n, a_seq, m, k, x_nums):
    print(f"a: {a_seq}")
    print(f"k: {k}")
    print(f"x: {x_nums}")
    result = ""
    for num in x_nums:
        shifts = 0
        cur_num = num
        x = a_seq[num - 1]
        previous = x
        idx = num - 2
        while idx > -1:
            if previous < a_seq[idx]:
                break
            elif previous > a_seq[idx]:
                cur_num = idx + 1
                previous = a_seq[idx]
            # previous == a_seq[idx]
            else:
                if shifts >= k:
                    break
                else:
                    cur_num = idx + 1
                    previous = a_seq[idx]
                    shifts += 1
            idx -= 1
        result += f"{cur_num} "
        # result.append(cur_num)

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
    # res_str = " ".join(list(map(str, res)))
    print(f"Result: {res_str}, Answer: {result_list[ii]}, Right: {res_str == result_list[ii]}")
