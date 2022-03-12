def get_different_length(woods):
    woods.sort()
    Max_difference = max(woods) - min(woods)
    Min_difference = 114514
    for i in range(1, len(woods)):
        if woods[i] - woods[i - 1] < Min_difference:
            Min_difference = woods[i] - woods[i - 1]
    return Max_difference - Min_difference


def get_range_number(woods):
    result_length = (woods[-1] + 2) // 3
    result = [0 for _ in range(result_length)]
    for elements in woods:
        result[(elements - 1) // 3] += 1
    return result

    
def get_M_longest_woods(woods, M):
    if len(woods) < M:
        return [-1]
    else:
        longest_logs = sorted(woods, reverse = True)
        result = [0 for _ in range(M)]
        for n in range(M):
            result[n] = longest_logs.index(woods[n])
        return result


def remove_M_longest_woods(woods, M):
    if len(woods) < M:
        return woods
    else:
        copy = sorted(woods, reverse = True)
        longest_logs = []
        for n in range(M):
            longest_logs.append(copy[n])
        result = []
        for logs in woods:
            if logs not in longest_logs:
                result.append(logs)
                result.sort()
        return result

def func(orders, woods):
    ans = []
    r1=get_different_length(woods)
    r2=get_range_number(woods)
    for order in orders:
        if order[0] == 0:
            ans.append(get_M_longest_woods(woods, order[1]))
        elif order[0] == 1:
            left_woods = remove_M_longest_woods(woods, order[1])
            ans.append(left_woods)
            woods = []
            for left_wood in left_woods:
                woods.append(left_wood)
    ans2=[r1]
    ans2.append(r2)
    ans2.append(ans)
    return ans2


def str_to_1DList(str):
    ans = []
    buf = ''
    for i in range(1, len(str) - 1):
        if str[i] == ',':
            ans.append(int(buf))
            buf = ''
        else:
            buf += str[i]
    ans.append(int(buf))
    return ans


def str_to_2DList(str):
    ans = []
    for i in range(1, len(str) - 1):
        if str[i] == '[':
            buf = ''
            p = i
            while str[p] != ']':
                buf += str[p]
                p += 1
            buf += str[p]
            ans.append(str_to_1DList(buf))
    return ans


orders = str_to_2DList(str(input().strip('"').replace(' ', '')))
woods = str_to_1DList(str(input().strip('"').replace(' ', '')))
print(func(orders, woods))
