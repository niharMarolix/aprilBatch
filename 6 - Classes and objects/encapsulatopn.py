class Car:
    def __init__(self, brand, model):
        self._brand = brand #protected variable
        self.__model = model # private variable
    def startEngie(self):
        return("engine started")
    def _drive(self):
        return("i am driving the car")
    def __stop(self):
        return("I am stopping the car")

car1 = Car("Maruti","Omni")
# # print(car1.brand)
# print(car1.startEngie())
# print(car1._drive())
print(car1.__stop())