
class Number():
    def __init__(self):
        self.num = 0
    def increase(self):
        self.num += 1
    def decrease(self):
        self.num -= 1




class NewNumber(Number):
    def __init__(self):
        super().__init__()
    def sho_val(self):
        print('Value:' +str(self.num))

    


num = NewNumber()
num.increase()
num.increase()
num.sho_val()
