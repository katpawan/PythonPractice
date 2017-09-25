class Employee:
    """This is dummy documentation for my Demo
       Class....learning OOPS in python!!!"""
    count = 0

    def __init__(self, name, salary):
        print('in parent\'s constructor')
        self.name = name
        self.salary = salary
        Employee.count += 1

    def getEmployeeCount(self):
        return Employee.count

    def displayEmployeeInfo(self):
        print("Name: %s Salary: %d" % (self.name, self.salary))

    def __del__(self):
        print('parent\'s destructor', self)


def main():
    print("Before any object", Employee.count)
    emp1 = Employee(salary=30000, name="Pawan")
    print("After first object", Employee.count)
    emp2 = Employee("Lokesh", 10000)
    print("After second object", Employee.count)
    emp1.displayEmployeeInfo()
    emp2.displayEmployeeInfo()
    if(hasattr(emp2, 'salary')):
        print(emp2.salary)
    print(getattr(emp2, 'name'))
    # this will create age in emp2 only and not in other objects of class
    setattr(emp1, "age", 23)
    print(emp1.age)
    # print(emp2.age)


if __name__ == '__main__':
    main()
