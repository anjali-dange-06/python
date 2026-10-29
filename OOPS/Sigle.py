# Single Level Inheritance in Python

# Parent Class
class Animal:
    def eat(self):
        print("Animal is eating")


# Child Class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")


# Main Program
d = Dog()

d.eat()
d.bark()