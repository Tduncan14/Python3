

# def info(**kw):

#    for k,v in kw.items():
#      print(k, ':', v)







# info(name='Jake', age=17, marks=88)



def addition(*n):
    sm = 0
    for num in n :
        sm += num
    return sm




sum = addition(12,45,77,32,2)


print(sum)