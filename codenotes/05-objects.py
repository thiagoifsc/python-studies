#examples of built in objects and methods
print(len("Test"))
print("Test".islower())
print("12341234".replace("3", "9"))


#defining an new class
class Car:
    speed = 0
    started = False

    def start(self):
        self.started = True
        print("Car started")

    def increase_speed(self, delta):
        if self.started:
            self.speed += delta
            print("Speed=", self.speed)
        else:
            print("Car not started")

    def stop(self):
        self.speed = 0
        print("Halting")

#creating an car object
car = Car()
car.increase_speed(20)
car.start()
car.increase_speed(30)
car.increase_speed(10)
car.stop()