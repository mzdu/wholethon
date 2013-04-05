# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):
    num1 = bigger(a,b)
    num2 = bigger(a,c)
    num3 = bigger(b,c)
    max1 = biggest(a,b,c)
    if num1 < max1:
        return num1
    elif num2 < max1:
        return num2
    elif num3 < max1:
        return num3
    else:
        return max1

#print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

#print(median(7,8,7))
#>>> 7



