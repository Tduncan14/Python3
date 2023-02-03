# class Algebra():
#     def __init__(self,r=0.0,i=0.0):
#         self.real = r
#         self.imag = i

#     def __add__(self,y):
#         self.real = self.real + y.real
#         self.imag = self.imag + y.imag
#         return(self)
#     def __sho_val__(self):
#         print(self.real, self.imag)


# num = Algebra(2.5, 6.25)
# num2 = Algebra(1.45,3.35)
# num3 = num + num2

# num3.__sho_val__()

# # print(num.real+ num2.real)


class Numeric_str():
    def __init__(self,Str = ''):
        self.Str = Str
    def __int__(self):
        return int(self.Str)




num = Numeric_str('1024')
pro = int(num.Str)*2

print(pro)

print(num.Str*2)