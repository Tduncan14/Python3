class Coder():
    def _init__(self,name):
        self.name = name
    def get_lang(self,lang):
        self.lang = lang





def is_pythonner(Lst):
    if 'Python' in Lst:
        print(True)
    else:
        print(False)




cd = Coder()
cd.get_lang(['Python','C'])

print(cd.lang)
