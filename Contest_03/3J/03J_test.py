# Created by Nikolay Pakhomov 12.11.2024
def find_min(n, height, chairs):
    result = 2
    return result


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

ans = find_min(chairs_len, vas_h, zipped)
print(ans)

for ii in range(test_n):
    res = find_min(n_list[ii], h_list[ii], zipped_list[ii])
    print(f"Result: {res}, Answer: {result_list[ii]}, Right: {str(res) == result_list[ii]}")
