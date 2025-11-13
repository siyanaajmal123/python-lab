class Employee:
    def __init__(self,id,name,dept,salary):
        self.id=id
        self.name=name
        self.dept=dept
        self.salary=salary
    def displayemp(self):
        print("employee id:",self.id)
        print("name:",self.name)
        print("department:",self.dept)
        print("salary:",self.salary)

emp1=Employee(1234,"jhon","HR",350000)
emp2=Employee(7645,"Liya","Accountant",250000)

emp1.displayemp()
emp2.displayemp()
