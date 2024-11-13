# Created by Nikolay Pakhomov 12.11.2024
def find_min(n, height, chairs):
    chairs = sorted(chairs, key=lambda x: (x[0]))
    discomfort = 1000000000
    left = right = sum_w = 0
    deq = []
    while left < n:
        if sum_w < height and right < n:
            sum_w += chairs[right][1]
            dis, idx = (0, left) if right - left == 0 else (chairs[right][0] - chairs[right - 1][0], right - 1)
            if len(deq) > 0:
                j = len(deq) - 1
                while j > -1 and deq[j][0] <= dis:
                    deq.pop(j)
                    j -= 1
            deq.append((dis, idx))
            if chairs[right][1] >= height:
                deq.append((0, right))
            right += 1
        if sum_w < height and right >= n:
            break
        if sum_w >= height:
            if len(deq) > 0:
                max_shift = deq[0]
                discomfort = min(max_shift[0], discomfort)
                if max_shift[1] == left:
                    deq.pop(0)
            sum_w -= chairs[left][1]
            left += 1
    return discomfort


n_list = []
h_list = []
zipped_list = []
result_list = []
with open("input_test.txt") as f:
    test_n = int(f.readline().strip())
    for ii in range(test_n):
        f.readline()
        chairs_len, vas_h = map(int, f.readline().split())
        zipped = list(zip(list(map(int, f.readline().split())), list(map(int, f.readline().split()))))
        n_list.append(chairs_len)
        h_list.append(vas_h)
        zipped_list.append(zipped)

with open('output_test.txt') as f:
    for ii in range(test_n):
        result_list.append(f.readline().strip())

for ii in range(test_n):
    res = find_min(n_list[ii], h_list[ii], zipped_list[ii])
    print(f"Result: {res}, Answer: {result_list[ii]}, Right: {str(res) == result_list[ii]}")
