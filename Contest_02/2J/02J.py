# Created by Nikolay Pakhomov 27.10.2024
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


with open("input2.txt") as f:
    a_len = int(f.readline())
    a_list = list(map(int, f.readline().split()))
    x_len, max_shifts = map(int, f.readline().split())
    x_list = list(map(int, f.readline().split()))

ans = get_evidence_list(a_len, a_list, x_len, max_shifts, x_list)
# print(" ".join(list(map(str, ans))))
print(ans.strip())
