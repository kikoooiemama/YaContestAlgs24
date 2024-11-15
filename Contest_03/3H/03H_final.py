# Created by Nikolay Pakhomov 04.11.2024
def rsq(p_sum, left, right):
    return p_sum[right] - p_sum[left]


prefix_sum = [0]
stack = []
with open("input.txt") as f:
    n = int(f.readline().strip())
    for i in range(n):
        operation = f.readline().strip()
        if operation.startswith("+"):
            x = int(operation)
            stack.append(x)
            prefix_sum.append(x + prefix_sum[-1])
        elif operation.startswith("?"):
            k = int(operation[1:])
            print(rsq(prefix_sum, len(stack) - k, len(stack)))
        else:
            prefix_sum.pop()
            print(stack.pop())
