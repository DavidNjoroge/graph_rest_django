#!usr/bin/env python2.7
def move_zeros(array):
    # while array.index(0):
    # print array
    new_array=[]
    zeros=[]
    # for item in range(array.count(0)):
    for item in array:
        if item==0 and type(item)!= bool:
            zeros.append(item)
            continue
        new_array.append(item)
        # print array
        # try:
        # position = array.index(0)
        # array.pop(position)
        # array.append(0)
        # except:
            
    print new_array+zeros




move_zeros([1,2,0,1,0,1,0,False,3,0,1,False,])
