# väike cheat sheet mulle kui ma unustan kuidas classid töötavad


### *CLASS ATTRIBUTE = attributes created in __init__ are called instance attributes.
#an instance attribute’s value is specific to a particular instance of the class.
#all Dog objects have a name and an age, but the values for the name and age attributes will vary depending on the Dog instance.

### *SELF PARAMETER = the instance is passed to the self paramter, so that new attributes can be defined on the object.

### *SELF.NAME = creates an attribute called name, assigns to it the value of the name

### *INSTANCE METHOD = now if buddy is called with description: buddy.description(),
# it will return "Buddy says BARK BARK", with instance methods we shall not forget
# parantheses!!! also in our case "BARK BARK" has to be passed in!

### *NEW INSTANCE = creates new Dog instance for a nine-year-old dog named "Buddy"

### *CHANGING VALUE = this changes the .age attribute of the buddy to 10

### *CHILD CLASS =to create a child class,
# you create new class with its own name and then put the name of the parent class in parentheses


class Dog:


  species = "Canis familiaris" # *CLASS ATTRIBUTE
  
  def __init__(self, name, age): # *SELF PARAMETER
    self.name = name #*SELF.NAME
    self.age = age

  def barking(self, sound): # INSTANCE METHOD
    return f"{self.name} says {sound}"

  def __str__(self):
    return f"{self.name} is {self.age} years old"


class Labrador(Dog): # *CHILD CLASS
  
  def barking(self, sound="Auh auh"):
    return f"{self.name} says {sound}"

buddy = Labrador("Buddy", 9) # *NEW INSTANCE
john = Dog("john", 3)

print(buddy.age)
buddy.age = 10 # *CHANGING VALUE
print(buddy.age)

print(john.barking("inputted bark"), buddy.barking())
