class Vehicle:
  def general_usage(self):
    print("general use: transportation")

class Car(Vehicle):
  def __init__(self):
    self.wheels = 4
    self.has_roof = True

  def specific_usage(self):
    print("specific use: use commute to work, vacation with family")

class MotorCycle(Vehicle):
  def __init__(self):
    self.wheels = 2
    self.has_roof = False

  def specific_usage(self):
    self.general_usage()
    print("specific use: road trip, racing")

car = Car()
car.general_usage()
car.specific_usage()

motor_cycle = MotorCycle()
motor_cycle.specific_usage()

# check instance
print(isinstance(car, Car))

# check subclass
print(issubclass(Car, Vehicle))