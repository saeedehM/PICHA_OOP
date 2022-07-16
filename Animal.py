# Dog Class
class Dog:
    # this method is called whenever Dog is instantiated
    def __init__(self, name, age):
        # create an attribute of the class dog which is name
        self.name = name
        self.age = age

    def add_one(self, x):
        return x + 1

    # operations that can be performed by Dog
    def bark(self):
        print("bark")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


# create Instance
d = Dog("Tim", 2)
d.set_age(23)
d2 = Dog("Bill", 13)
print(d.name)
print(d2.name)
d.bark()
print(d.add_one(4))
print(type(d))

