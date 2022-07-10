class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("IDK")


class Cat(Pet):
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")


class Dog(Pet):
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    def speak(self):
        print("Bark")


class Fish(Pet):
    pass


p = Pet("Tim", 19)
p.show()
p.speak()

c = Cat("Bill", 34, "Brown")
c.show()
c.speak()

d = Dog("Mark", 76)
d.show()
d.speak()

f = Fish("Bubbles", 3)
f.speak()
