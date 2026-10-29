# Parent Class
class Animal:
    def eat(self):
        print("Animal is eating")


# Two Child Classes
class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Cat(Animal):
    def meow(self):
        print("Cat is meowing")


# Multiple Inheritance
class Puppy(Dog, Cat):
    def play(self):
        print("Puppy is playing")


# Main Program
p = Puppy()
p.eat()
p.bark()
p.meow()
p.play()