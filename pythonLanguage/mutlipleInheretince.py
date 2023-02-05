

class Coder():
    def __init__(self):
        self.name = input("name")


class Pythoneer():
    def __init__(self):
        self.works = input('Works')



class WebDev(Coder,Pythoneer):
     def __init__(self):
        Coder.__init__(self)
        Pythoneer.__init__(self)
     def start_now(self):
        print('new.html @Django')




web = WebDev()
web.start_now()