
from random import randint

def bubble_sort(nums):  
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True


# Verify it works
random_list_of_nums = []
for i in range(10):
    random_list_of_nums.append(randint(1, 100))

print "Before sort: ", random_list_of_nums
bubble_sort(random_list_of_nums)  
print "After sort: ", random_list_of_nums

