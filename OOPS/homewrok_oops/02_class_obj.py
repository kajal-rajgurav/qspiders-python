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
