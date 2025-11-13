class Student:
    def __init__(self ,rno,name,course):
        self.rno=rno
        self.name=name
        self.course=course
    def displaystudent(self):
        print("roll number:",self.rno)
        print("name:",self.name)
        print("course:",self.course)
stud1=Student(10,"jack","MCA")
stud2=Student(11,"George","MCA")

stud1.displaystudent()
stud2.displaystudent()
