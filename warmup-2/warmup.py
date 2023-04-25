#https://codingbat.com/prob/p145834
def string_times(str, n):
    """Given a string and a non-negative int n,  return a larger string that is n copies of the original string. """
    return str * n


print(string_times('Hi', 2))
print(string_times('Hi', 3))
print(string_times('Hi', 1))

def string_splosion(str):
  result = ""
  for i in range(len(str)):
    result += str[:i+1]
  return result


def array_front9(nums):
  end = len(nums)
  if end > 4:
    end = 4
  for i in range(end):
    if nums[i] == 9:
      return True
  return False


def front_times(str, n):
  front = str[:3]
  result = ""
  for i in range(n):
    result += front
  return result

def last2(str):
  if len(str) < 2:
    return 0
  last2 = str[-2:]
  count = 0
  for i in range(len(str)-2):
    if str[i:i+2] == last2:
      count += 1
  return count


def array123(nums):
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False

def string_bits(str):
    result = ""
    for i in range(0, len(str), 2):
        result += str[i]
    return result

def array_count9(nums):
    count = 0
    for num in nums:
        if num == 9:
            count += 1
    return count


def string_match(a, b):
    count = 0
    for i in range(len(a)-1):
        if a[i:i+2] == b[i:i+2]:
            count += 1
    return count
