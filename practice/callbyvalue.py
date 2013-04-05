p = [1,2,3,4,5]
q = ['a','b']

# this will change the value of a[0]
def func1(a):
    a[0] = 12

#func1(p)
#print p 



# this will change the actual value of a list    
def func2(a):
    a[0] = a[0] + a[1]



def func3(a):
    b = []
    while a:
        b.append(a.pop())
        print a, b 

     

#func3(p)
#print p 

#===============================================================================
# [1, 2, 3, 4] [5]
# [1, 2, 3] [5, 4]
# [1, 2] [5, 4, 3]
# [1] [5, 4, 3, 2]
# [] [5, 4, 3, 2, 1]
# []
#===============================================================================


# this procedure will list-q, but will not affect list-p
def func4(a, b):
    b[0] = 3
    a = b 
    
func4(p, q)
print q 
print p






