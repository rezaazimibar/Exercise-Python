# class Cars:
#     isThisCar = True
#
#     def __init__(self, model="noneYet", speed="0"):
#         self.models = model
#         self._speeds = speed
#
#     def run(self):
#         print("running")
#         print(self.isThisCar)
#
#     def explain(self):
#         print(f"the name of car is {self.models} and  \n car speed power of 10 is {self._speeds ** 10}")
#
#     @classmethod
#     def addthings(cls, num1, num2):
#         return cls("BMW", num1 + num2)
#
#
# car1 = Cars("pride", 125)
#
# print(car1._models)

# print(car1.models)
# print(car1.speeds)
# print(f"is this car:{car1.run()}")
# print(Cars.addthings(5, 4).speeds)
# car2 = Cars.addthings(34, 55)
# print(car2.models)
# car2.explain()
# car3=Cars("nothing",3)
# car3.explain()
# /////////////////////////////////////////////////////////////
class User:
    def __init__(self, email="no email"):
        self.email = email

    def logging(self):
        print("your logging is successful")

    def speak(self):
        print(f"i'm just regular user")


class Dragon(User):
    def __init__(self, name, attack, email):
        super().__init__(email)
        self.name = name
        self.attack = attack

    def speak(self):
        print(f"my name is {self.name} and my attack is {self.attack} and {self.logging()}")


class Wizard(User):
    def __init__(self, name, attack, email):
        super().__init__(email)
        self.name = name
        self.attack = attack

    def speak(self):
        User.speak(self)
        print(f"im wizard my name is🔥🔥 {self.name} and my attack is {self.attack}")


dragon1 = Dragon("reza", 500, "wwwbeta04")
wizard1 = Wizard("ali", 250,"emailwizar")
print(dragon1.email)
for char in wizard1, dragon1:
    char.speak()
print(dir(dragon1))
