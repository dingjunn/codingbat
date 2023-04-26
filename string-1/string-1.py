def hello_name(name):
    """Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!"."""
    return 'Hello ' + name + '!'


print(hello_name('Bob'))
print(hello_name('Alice'))
print(hello_name('X'))

def make_abba(a, b):
    """Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi"""

    return a + b + b + a


def make_tags(tag, word):
    return "<{0}>{1}</{0}>".format(tag, word)

def make_out_word(out, word):
    return out[:2] + word + out[2:]


def extra_end(str):
    return str[-2:] * 3


def first_two(str):
    return str[:2]

def first_half(str):
    return str[:len(str)//2]

def without_end(str):
    return str[1:-1]

def combo_string(a, b):
    if len(a) < len(b):
        shortstr = a
        longstr = b
    else:
        shortstr = b
        longstr = a
    
    return shortstr + longstr + shortstr

def non_start(a, b):
    return a[1:] + b[1:]

def left2(str):
    return str[2:] + str[:2]

