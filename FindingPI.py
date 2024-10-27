import random

def pi_one(e):
    """ returns estimated value of pi using a while loop
        input e: float (the acceptable difference between estimated pi and actual pi)
    """
    circle_area = 0
    square_area = 0
    pi_estimate = 0
    actual_pi = 3.141592653589793
    
    while abs(pi_estimate - actual_pi) > e:
        x = round(random.uniform(-1,1), 1)
        y = round(random.uniform(-1,1), 1)
        
        if (x**2 + y**2 <= 1):
            circle_area += 1
            square_area+=1
        else:
            square_area += 1

        pi_estimate = (4 * circle_area) / square_area
    
    return pi_estimate


def pi_two(n):
    """ returns estimated value of pi using a for loop
        input n: int (number of darts to throw)
    """
    circle_area = 0
    square_area = 0
    for i in range(n):
        x = round(random.uniform(-1,1), 1)
        y = round(random.uniform(-1,1), 1)
        if (x**2 + y**2 <= 1):
            circle_area+=1
            square_area+=1
        else:
            square_area+=1
    return (4 * circle_area)/square_area

avg = sum([pi_two(100) for i in range(1000)])/1000
print(avg)

print(pi_one(.0001))

rows = 0
for i in range(1, 4):
    for j in range(i):
        print(i, j)
        rows+=1

print(rows)
