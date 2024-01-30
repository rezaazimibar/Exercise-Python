class Cars:
    isThisCar = True

    def __init__(self, model, speed):
        self.models = model
        self.speeds = speed

    def run(self):
        print("running")


car1 = Cars("pride", 125)
print(car1.models)
print(car1.speeds)
print(car1.isThisCar)
