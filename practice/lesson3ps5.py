

udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(list1):
    student_num = 0
    tuition = 0
    
    for sub_list in list1:
        student_num = student_num + sub_list[1]
        tuition = tuition + sub_list[2] * sub_list[1]
                
    return student_num, tuition

def total_enrollment2(list2):
    student_num = 0
    tuition = 0
    
    for univ_name, student_num, tuition in list2:
        print univ_name
        annual_income = student_num * tuition
        print annual_income
                
    return annual_income

#print total_enrollment(udacious_univs)
#>>> (90000,0)
#
# The L is automatically added by Python to indicate a long
# number. If you are trying the question in an outside 
# interpreter you might not see it.
#
print total_enrollment2(usa_univs)
#>>> (77285,3058581079L)

#def func1(list1):
#    
#    for sub_list in list1:
#        print sub_list
#        for item in sub_list:
#            print item
#            
#
#func1(udacious_univs)
