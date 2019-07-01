
from random import randint

list_to_sort = []
for i in range(10):
    list_to_sort.append(randint(0, 100))

print "List to sort: ", list_to_sort

def merge_sort(list_to_sort):
    if len(list_to_sort) < 2:
        return list_to_sort

    mid_index = len(list_to_sort) / 2
    left = list_to_sort[:mid_index]
    right = list_to_sort[mid_index:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    sorted_list = []
    current_left_index = 0
    current_right_index = 0

    while len(sorted_list) < len(left) + len(right):
        if ((current_left_index < len(left)) and
            (current_right_index == len(right) or
             sorted_left[current_left_index] < sorted_right[current_right_index])):
            sorted_list.append(sorted_left[current_left_index])
            current_left_index += 1
        else:
            sorted_list.append(sorted_right[current_right_index])
            current_right_index += 1

    return sorted_list


print "Sorted List: ", merge_sort(list_to_sort)
