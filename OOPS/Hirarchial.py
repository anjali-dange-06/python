# Parent Class
class Animal:
    def eat(self):
        print("Animal is eating")


# First Child Class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")


# Second Child Class
class Cat(Animal):
    def meow(self):
        print("Cat is meowing")


# Main Program
d = Dog()
d.eat()
d.bark()

c = Cat()
c.eat()
c.meow()