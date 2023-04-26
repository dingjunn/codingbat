def double_char(str):
    """Given a string, return a string where for every  char in the original, there are two chars."""
    new_str = ''
    for letter in str:
        new_str += letter * 2
    return new_str


print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi, there'))

def count_code(str):
    count = 0
    for i in range(len(str)-3):
        if str[i:i+2] == 'co' and str[i+3] == 'e':
            count += 1
    return count


def count_hi(string):
    count = 0
    for i in range(len(string) - 1):
        if string[i:i+2] == "hi":
            count += 1
    return count

def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return a.endswith(b) or b.endswith(a)

def cat_dog(str):
  cat_count = 0
  dog_count = 0
  for i in range(len(str)-2):
    if str[i:i+3] == 'cat':
      cat_count += 1
    elif str[i:i+3] == 'dog':
      dog_count += 1
  return cat_count == dog_count


def xyz_there(str):
  for i in range(len(str)-2):
    if str[i:i+3] == 'xyz' and (i == 0 or str[i-1] != '.'):
      return True
  return False
