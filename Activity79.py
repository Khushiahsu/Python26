#Write a program to create a class with the name Student and perform the following tasks - 1. Declare a variable grade 2. Print a sentence inside the class 3. Create an object of class student and see the output?

class student:
   
     def __init__(self,grade):
          self.grade=grade
          print('Aarav is in the',self.grade,'grade')
obj1 = student(0)
          