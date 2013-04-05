# the item and list1 are all changing druing the loop

list1 = ['1','11','111','1111']
list2 = ['a', 'b']

for item in list1:
    print 'item is ' + item
    print 'pop is ' + list1.pop(0)
    print 'list1 is ' + str(list1)
    