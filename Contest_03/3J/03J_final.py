# Created by Nikolay Pakhomov 04.11.2024
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


with open("input.txt") as f:
    chairs_len, vas_h = map(int, f.readline().split())
    zipped = list(zip(list(map(int, f.readline().split())), list(map(int, f.readline().split()))))

ans = find_min(chairs_len, vas_h, zipped)
print(ans)
