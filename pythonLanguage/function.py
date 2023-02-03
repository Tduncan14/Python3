
class Coder():
    def __init__(self,name):
        self.Name = name

    def info(self):
        print(self.Name)

    def is_pythonner(self):
        if'Python' in self.language:
            print(True)
        else:
            print(False)



cd = Coder('Treek')
 
cd.language = ['C','Python']
cd.is_pythonner()


print(cd.Name)
# print(cd.info())