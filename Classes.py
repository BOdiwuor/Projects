# Create your class here
#class name is always capitalized

#Instance attribute : It is specific to each instance of the class. 
#Insance attributes in Python are typically defined within the contstructor method (i.e __init__)
#The self keyword defines these attributes within the constructor method

class Car:
    def __init__(self, brand):
        self.brand = brand

car1 = Car("Toyota")
car2 = Car("Benz")

print(car1.brand)
print(car2.brand)


class Facade:
  pass

#create an instance of the Facade class by adding parentheses to the name of the class.
#The instance is assigned to a variable so that it can be accessed at a later time
facade_1 = Facade()




class Cat:
  def __init__(self, input_name, input_age = 0, input_does_it_shed = True):
    self.name = input_name
    self.age = input_age
    self.shed = input_does_it_shed

# add a method to the code that changes the cats atrribute
  def meow(self):
    self.age = self.age + 1
    print("{name} meows at {age} years old.".format(name = self.name, age = self.age))


cat_one = Cat("Sue", 12, False)
cat_one.meow()
# Call your method on your
# new pet here.


#Add a method that has the two pets interact with each other. This will likely have the format pet_one.method_name(pet_two).


class Cat:
  def __init__(self, input_name, input_age = 0, input_does_it_shed = True):
    self.name = input_name
    self.age = input_age
    self.shed = input_does_it_shed
    self.sheds_with = []
  # Create method where two
  # pets interact.
  # Ex: def name(self, pet):
  def interact(self, other_cat):
    #the code below is accompanies the 'shed' attribute that is defined in the class
      if other_cat.shed:
      # If the other cat sheds,
      # it adds other_cat to its list
        self.sheds_with.append(other_cat)
      # The other cat also adds this 
      #specific cat to its list
        other_cat.sheds_with.append(self)
        print("{name} can make friends with {other_name}!".format(name = self.name, other_name = other_cat.name))
      else:
       # If the other cat does NOT shed,
      # no one becomes friends.
        print("{other_name} did not want to become friends with {name}!".format(name = self.name, other_name = other_cat.name))

cat_one = Cat("Sue", 12, False)
cat_two = Cat("Angola", 13, True)

cat_one.interact(cat_two)



# Create two pets.


# Call your method below.

#Add a constructor to our Circle class.

#Now have the constructor print out the message "New circle with diameter: {diameter}" when a new circle is created.

#Create a circle teaching_table with diameter 36.

class Circle:
  pi = 3.14
  
  
  # Add constructor here:
  def __init__(self, diameter):
    pass
    self.diameter = diameter
    print("New circle with diameter: {diameter}".format(diameter = self.diameter))

teaching_table = Circle(36)

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
  if hasattr(element,"count"):
     print(str(type(element)) + " has the count attribute!")
  else:
     print(str(type(element)) + " does not have the count attribute :")


class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter / 2

  def circumference(self):
    return 2 * self.pi * self.radius

#Define three Circles with three different diameters. i.e. define 3 objects
medium_pizza = Circle(12)

teaching_table = Circle(36)

round_room = Circle(11460)

#print out the circumferences of medium_pizza, teaching_table, and round room. You will need to call the .circumference() method on each of the three instances above

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())


#Define a class named Student that will be our data model at Jan van Eyck High School and Conservatory.Add a constructor for Student. Have the constructor take in two parameters: a name and a year. Save those two as attributes .name and .year.

#In Python, instance methods within a class must take self as the first parameter to refer to the instance itself

class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  def add_grade(self, grade):
    if isinstance(grade, Grade):
       self.grades.append(grade)
    else:
      pass
  def get_average(self):
    return avg(self.score)


#create three instances of the Student class:
#When you're creating instances of the Student class, you need to pass strings as arguments

roger =  Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

#Create a Grade class, with .minimum_passing as an attribute set to 65 (class variable).This attribute will be used by all instances of the class

#Write a Grade method .is_passing() that returns whether a Grade has a passing .score.

class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score
  def is_passing(self):
    if self.score >= Grade.minimum_passing:
      return True
    else:
      return False
     
  

#You can create a new instance of the Grade class by calling Grade(score). After creating this instance, you can add it to pieter‘s grades using the .add_grade() method we defined in the Student class.

new_grade = Grade(100)
pieter.add_grade(new_grade)





