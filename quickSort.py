#! /usr/bin/env python


def quickSort(mylist):
    if len(mylist) < 2:
        return mylist
    else:
        pivot = mylist[0]
        smaller = [x for x in mylist[1:] if x <= pivot]
        greater = [x for x in mylist[1:] if x > pivot]
    return quickSort(smaller) + [pivot] + quickSort(greater)

if __name__ == "__main__":
    mylist = [167,234,56,353,55,87,21,456]
    print(quickSort(mylist))