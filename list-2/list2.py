def count_evens(nums):
    """Return the number of even ints in the given array.

    Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
    """
    evens = 0
    for number in nums:
        if number % 2 == 0:
            evens += 1
    return evens


print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))


def sum13(nums):
    """
    Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
    """
    if len(nums) == 0:
        return 0

    total = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2
        else:
            total += nums[i]
            i += 1

    return total

def big_diff(nums):
    return max(nums) - min(nums)


def sum67(nums):
    ignore = False
    total = 0
    for num in nums:
        if num == 6:
            ignore = True
        elif num == 7 and ignore:
            ignore = False
        elif not ignore:
            total += num
    return total

def centered_average(nums):
    nums.sort()
    sum = 0
    for i in range(1, len(nums)-1):
        sum += nums[i]
    return sum // (len(nums)-2)


def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i] == 2:
            return True
    return False
