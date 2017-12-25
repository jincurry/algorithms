#! /usr/bin/env python


def recursive_sum(my_list):
    if my_list == []:
        return 0
    return my_list[0] + recursive_sum(my_list[1:])

if __name__ == "__main__":
    # 最大递归的深度为996
    listed = [x for x in range(997)]
    # print(listed)
    total = recursive_sum(listed)
    print(total)
