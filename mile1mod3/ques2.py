class Animal:
    def eat(self):
      print('Animal eats food')

class Mammal(Animal):
  def walk(self):
    print('Mammal walks with legs')

class Dog(Mammal):
  def bark(self):
    print('Dog barks at strangers')
dog1 = Dog()
dog1.eat()
dog1.walk()
dog1.bark()


class Calculator:
  def add(self, a,b,c=0):
    return a+b+c

class AdvancedCalculator(Calculator):
  def add(self, *numbers):
        return sum(numbers)

calc = Calculator()
print("Calculator:", calc.add(1, 2))
print("Calculator:", calc.add(1,2,3))

adv_calc = AdvancedCalculator()
print("AdvancedCalculator:", adv_calc.add(5, 6))
print("AdvancedCalculator:", adv_calc.add(5, 6, 7, 8, 9))