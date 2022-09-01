class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is", self.name,"and my age is", self.age)


p1 = Person("Sagar", 29)

p1.myfunc()
del p1.age
print(dir(p1))

p2 = Person("Prafull", 28)
p2.myfunc()
print(dir(p2))

print(dir(Person))
# p1.myfunc()
