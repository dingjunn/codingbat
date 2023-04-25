def makes10(a, b):
    """Return True if one of the integers is 10 or if their sum is 10."""
    return a == 10 or b == 10 or a + b == 10
    
print(makes10(9,10))

name = "dingjun"
print('\n'.join([''.join([(name[(x-y) % len(name)] if str(((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3-0.00001).startswith('-') else ' ') for x in range(-30, 30)]) for y in range(15, -15, -1)]))