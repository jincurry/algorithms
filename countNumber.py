#! /usr/bin/env python


def count_list(my_list):
    if my_list == []:
        return 0
    return 1 + count_list(my_list[1:])

def max_num(mylist):
    if len(mylist) == 2:
        return mylist[0] if mylist[0] > mylist[1] else mylist[1]
    sub_max = max_num(mylist[1:])
    return mylist[0] if mylist[0] > sub_max else sub_max

if __name__ == "__main__":
    listed = [x for x in range(456)]
    print(count_list(listed))
    onelist = [1,2,43,654,765,12,57]
    print(max_num(onelist))