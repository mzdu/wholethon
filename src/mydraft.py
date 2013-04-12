list1 = "this is a sdtdring"
list2 = 'strq'

def func1(a,b):
    return 'not match' if ((item1 for item1 in list2).find(item2) for item2 in list1)==-1 else 'match'

print func1(list1,list2)    