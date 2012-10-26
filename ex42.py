## Animal is-s object
class Animal(object):
    pass
    
## Dog is-a class
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a function named __init__ with parameters self, name
        self.name = name
        
## cat is-a class
class Cat(Animal):

    def __init__(self, name):
        ## cat has-a function named __init__ with parameters self, name
        self.name = name

## person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a function __init__ with parameters self, name
        self.name = name
        
        ## person has-a pet of some kind
        self.pet = None
        
## Employee is-a class
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has-a function __init__  with self, name, salary??
        super(Employee, self), __init__(name)
        ## from self get salary and set it to salary
        self.salary = salary
        
## Fish is-a object
class Fish(oject):
    pass
    
## Salmon is-a class
class Salmon(Fish):
    pass
    
## Halibut is-a class
class Halibut(Fish):
    pass
    
    
## rover is-a dog
rover = Dog("Rover")

## satan is-a Cat("Satan")
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## from mary get pet and set it to satan
mary.pet = satan

## frank is-a employee
frank = Employee("Frank", 120000)

## from frank get pet and set it to rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut()
harry = Halibut()


