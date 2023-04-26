def first_last6(nums):
    """Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more."""
    return nums[0] == 6 or nums[-1] == 6


print(first_last6([1, 2, 6]))
print(first_last6([6, 1, 2, 3]))
print(first_last6([13, 6, 1, 2, 3]))

#common end
def commonend(a, b):
    """
    Given two arrays of integers, returns True if they have the same first element or they have the same last element. 
    Both arrays will be length 1 or more.
    """
    return a[0] == b[0] or a[-1] == b[-1]


#reverse
def reverse3(nums):
    """
    Given an array of integers of length 3, returns a new array with the elements in reverse order.
    """
    return [nums[2], nums[1], nums[0]]

def middle_way(a, b):
    """
    Given two integer arrays of length 3, returns a new array containing their middle elements.
    """
    return [a[1], b[1]]

def same_first_last(nums):
    if len(nums) >= 1 and nums[0] == nums[-1]:
        return True
    else:
        return False

def sum3(nums):
    return sum(nums)

def max_end3(nums):
    max_val = max(nums[0], nums[-1])
    return [max_val, max_val, max_val]


def make_ends(nums):
    return [nums[0], nums[-1]]

def make_pi():
    return [3, 1, 4]

def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]

def sum2(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + nums[1]


def has23(nums):
    return 2 in nums or 3 in nums


