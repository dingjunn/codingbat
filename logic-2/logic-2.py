def lone_sum(a, b, c):
    """Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum."""
    l = [a, b, c]
    result = 0
    for x in l:
        if l.count(x) == 1:
            result += x
    return result


print(lone_sum(1, 2, 3))
print(lone_sum(3, 2, 3))
print(lone_sum(3, 3, 3))

def make_bricks(small, big, goal):
    return goal % 5 <= small and goal - big * 5 <= small


def lucky_sum(a, b, c):
    sum = 0
    if a == 13:
        return sum
    else:
        sum += a
        if b == 13:
            return sum
        else:
            sum += b
            if c == 13:
                return sum
            else:
                sum += c
    return sum

def no_teen_sum(a, b, c):
    def fix_teen(n):
        if n in [13, 14, 17, 18, 19]:
            return 0
        else:
            return n
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


def round_sum(a, b, c):
    def round10(num):
        if num % 10 >= 5:
            return num + (10 - (num % 10))
        else:
            return num - (num % 10)
    return round10(a) + round10(b) + round10(c)


def close_far(a, b, c):
    if abs(b-a) <= 1:
        # b is close to a
        if abs(c-a) >= 2 and abs(c-b) >= 2:
            # c is far from a and b
            return True
    elif abs(c-a) <= 1:
        # c is close to a
        if abs(b-a) >= 2 and abs(b-c) >= 2:
            # b is far from a and c
            return True
    return False


def make_chocolate(small, big, goal):
    max_big_bars = goal // 5
    if max_big_bars <= big:
        goal -= max_big_bars * 5
    else:
        goal -= big * 5

    if goal <= small:
        return goal
    else:
        return -1
