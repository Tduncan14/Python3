import threading

#threading allows us to spread by excuting multiple task at the same time
#

def function1():
    for i in range(10):
     print("One")





def function2():
     for i in range(10):
        print("TWO ")


def function3():
    for i in range(10):
      print("Three")




# 
# function1()
# function2()
# function3()


#we can execute to function currently using threads


t1 = threading.Thread(target = function1)
t2 = threading.Thread(target = function2)
t3 = threading.Thread(target=function3)



t1.start()
t2.start()
t3.start()


# threads can be only be used once . if you want to reuse you must redefine




#if you want to pasue the main progaim until a thread is done you can1



t1 = threading.Thread(target = function1)
t1.start()
t1.join() #this pauses the main porgam unil the thread is complete
print('thread rules')