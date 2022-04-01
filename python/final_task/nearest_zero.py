# ID посылки: 66651461
from typing import List


def get_nearest_zero(_list) -> List[int]:
    list_len = len(_list)
    zero_list = []
    for i in range(list_len):
        if _list[i] == 0:
            zero_list.append(i)
    if len(zero_list) == 1:
        for i in range(list_len):
            if _list[i] != 0:
                _list[i] = abs(i - zero_list[0])
    else:
        if zero_list[0] > 0:
            for i in range(zero_list[0]):
                _list[i] = zero_list[0] - i
        if zero_list[-1] < list_len - 1:
            for i in range(zero_list[-1] + 1, list_len):
                _list[i] = i - zero_list[-1]
        z = 0
        while z <= len(zero_list) - 2:
            left_zero = zero_list[z]
            right_zero = zero_list[z + 1]
            for i in range(left_zero + 1, right_zero):
                _list[i] = min(i - left_zero, right_zero - i)
            z += 1
    return _list


def read_input() -> List[int]:
    n = int(input())
    street_list = list(map(int, input().split()))
    return street_list


street_list = read_input()
print(" ".join(map(str, get_nearest_zero(street_list))))
