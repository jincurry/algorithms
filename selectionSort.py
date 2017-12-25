#! /usr/bin/env python
from numpy.random import random


def findSmaller(list):
    smallerElement = list[0]
    elementindex = 0
    for i in range(1, len(list)):
        if smallerElement >= list[i]:
            smallerElement = list[i]
            elementindex = i
    return elementindex


def selectionSort(list):
    sorted_list = []
    for i in range(len(list)):
        index = findSmaller(list)
        sorted_list.append(list[index])
        list.pop(index)
    return sorted_list


if __name__ == "__main__":
    my_list = [1,3,34,65,23,7,234,9]
    print(my_list)
    print(selectionSort(my_list))
