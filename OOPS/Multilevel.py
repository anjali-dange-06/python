# Parent Class
class Animal:
    def eat(self):
        print("Animal is eating")


# Child Class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")


# Grandchild Class
class Puppy(Dog):
    def weep(self):
        print("Puppy is weeping")


# Main Program
p = Puppy()
p.eat()
p.bark()
p.weep()