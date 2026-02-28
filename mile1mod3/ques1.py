class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print("car details: ","\n", self.brand, "\n", self.model, "\n", self.year)

Car1 = Car('Tesla', 'electric', 2026)
Car1.display_info()