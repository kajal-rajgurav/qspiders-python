class car:
    c_brand='tata'
    c_model='toyota'
    year=2011
    ceo='ratan tata'

# perspm


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

# created class using __init__ keyword
class Person:
  pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)

Using __init__() makes it easier to create objects with initial values:

Example
With __init__(), you can set initial values when creating the object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 28)

print(p1.name)
print(p1.age)
The self Parameter
The self parameter is a reference to the current instance of the class.

It is used to access properties and methods that belong to the class.

ExampleGet your own Python Server
Use self to access class properties:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()

Note: The self parameter must be the first parameter of any method in the class.

Why Use self?
Without self, Python would not know which object's properties you want to access:

Example
The self parameter links the method to the specific object:

class Person:
  def __init__(self, name):
    self.name = name

  def printname(self):
    print(self.name)

p1 = Person("Tobias")
p2 = Person("Linus")

p1.printname()
p2.printname()