

def product():
     prod = 12 * 15
     print(prod)




product()



def greet(name):
    print ('Have a nice day', str(name))



greet('treek')




def result(name = 'None', marks = None):
    if  name != 'None' or marks !=None :
        print('Name:' + str(name))
        print('Marks:' + str(marks))






result(name='treek', marks = 1)
result()