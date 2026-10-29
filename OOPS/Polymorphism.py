# POLYMORPHISM IN PYTHON

class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")


# Creating Objects
d = Dog()
c = Cat()

# Calling the Same Method
d.sound()
c.sound()