# coding: utf-8

object_list = [1, 8, 4, 3, 5, 2]


def backpack1(total, object_list):
    object_len = len(object_list)
    k = 0
    stack = []
    while stack or k < object_len:
        while total > 0 and k < object_len:
            if total >= object_list[k]:
                # stack.append(object_list[k])
                stack.append(k)
                total -= object_list[k]
            k += 1
        if total == 0:
            print stack
        # wight = stack.pop()
        # total += wight
        k = stack.pop()
        total += object_list[k]
        k += 1

backpack1(10, object_list)

