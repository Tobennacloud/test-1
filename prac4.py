class Students:
     def __init__(self, name):
          self.name = name
          self.points=0
          self.addedpoints=10

     def added(self, students_grade):
        students_grade.points=students_grade.points + self.addedpoints
       
x=Students("kitty" )  
y=Students("Danny") 
z=Students("fred ")

for i in range(10):
     
     print(x.name)
     y.added(x)

     print (x.points)








