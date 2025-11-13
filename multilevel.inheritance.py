class student:
     def getData(self,rollno,name,course):
         self.rollno=rollno
         self.name=name
         self.course=course
     def displaystudent(self):
         print("Roll Number:",self.rollno)
         print("Name",self.name)
         print("Course",self.course)


class Test(student):
    def getMarks(self,marks):
        self.marks=marks
    def displaymarks(self):
        print("Total marks:",self.marks)

class Result(Test):
    def calculateGrade(self):
        if self.marks>480: self.grade="Distinction"
        elif self.marks>360: self.grade="First Class"
        elif self.marks>240: self.grade="Second Class"
        else:self.grade="Failed"
        print("result",self.grade)


r=int(input("Enter rollno:"))
n=input("Enter name:")
c=input("Enter the course:")
m=int(input("Enter the marks:"))

print("RESULT")
stud1=Result()
stud1.getData(r,n,c)
stud1.getMarks(m)
stud1.displaystudent()
stud1.displaymarks()
stud1.calculateGrade()
