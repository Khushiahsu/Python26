#Write a program to create a class Parrot and perform the following tasks - 1. Create a class variable species 2. Create a __init__ method that has instance variables - name and age 3. Create instances of class Parrot, passing arguments as well 4. Print Class variable by accessing it 5. Print Instance variables as well
class parrot:
    species='bird'
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('The age of',self.name,'is',self.age)
obj1 = parrot('Jake','15')
    