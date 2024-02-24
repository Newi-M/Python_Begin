# Create class Person and define the attributes and methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print('My name is {}, I am {} years old.'.format(self.name, self.age))


# Create object person1 of class Person
person1 = Person("Any", 5)
print('Name: ', person1.name)
print('Age: ', person1.age)

person1.introduce()
