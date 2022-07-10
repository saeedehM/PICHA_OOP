class Cat:
    def __init__(self, n, c):
        self.name = n
        self.color = c

    def meow(self):
        print("meow")

    def add_one(self, i):
        return i + 1


c = Cat("Pishi", "white")
print(c.name)
print(c.color)
c.meow()
print(c.add_one(78))
c2 = Cat("Narenji", "orange")
print(c2.name)














x = "Hello"

y = 1

z = True

shoppingList = []
shoppingList.append("eggs")

numbers = [1, 3, 4, 5]
numbers.append(7)

print(type(numbers))
print(type(shoppingList))


def hello():
    print("hello")


print(type(hello))
# print(type(x))
#
# print(type(y))
#
# print(type(z))
#
# print(x+y)
