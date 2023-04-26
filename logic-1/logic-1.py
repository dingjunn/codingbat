def cigar_party(cigars, is_weekend):
    """When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and  60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise."""
    return is_weekend or (not is_weekend and 40 <= cigars <= 60)


print(cigar_party(30, False))
print(cigar_party(40, False))
print(cigar_party(50, False))
print(cigar_party(70, True))

#caught speeding
def caught_speeding(speed, is_birthday):
    """You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

"""
    if is_birthday:
        speed -= 5
    
    if speed <= 60:
        return 0
    elif speed <= 80:
        return 1
    else:
        return 2

def love6(a, b):
    if a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6:
        return True
    else:
        return False

def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1
    
def sorta_sum(a, b):
    if 10 <= a + b <= 19:
        return 20
    else:
        return a + b
    
def in1to10(n, outside_mode):
    if outside_mode:
        return n <= 1 or n >= 10
    else:
        return 1 <= n <= 10


def squirrel_play(temperature, is_summer):
    if is_summer:
        return temperature >= 60 and temperature <= 100
    else:
        return temperature >= 60 and temperature <= 90

def alarm_clock(day, vacation):
    if vacation:
        if day == 0 or day == 6:
            return "off"
        else:
            return "10:00"
    else:
        if day == 0 or day == 6:
            return "10:00"
        else:
            return "7:00"



def near_ten(num):
    return num % 10 <= 2 or num % 10 >= 8
