
# class Parent():
#     def 1
#     def 2
#     def 3




# class Child():


class Coder():
  def __init__(self):
    self.name = input('Name ')
    self.lang = input('Languages ')


  def sho_details(self):
     print('Name:'+ str(self.name))
     print('Langauges:'+ str(self.lang))



class Pythoneeer():
    def __init__(self):
        self.profile = Coder()
    def profiles(self):
        self.profile.sho_details()




Jake = Pythoneeer()
Jake.profiles()