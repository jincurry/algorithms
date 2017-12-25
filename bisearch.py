#! /usr/bin/env python
from random import random


def binary_search(list,target):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        print(mid)
        if target == list[mid]:
            return mid
        if target > list[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return None

if __name__ == "__main__":
    my_list = [x for x in range(100000000)]
    print(binary_search(my_list,397246))