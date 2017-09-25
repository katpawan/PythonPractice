from Employee import Employee
import n

class HSBCEmployee(Employee):
    """docstring for HSBCEmployee"""

    def __init__(self, name, salary, team):
        super(HSBCEmployee, self).__init__(name, salary)
        print('in child\'s  constructor')
        self.team = team

    def __del__(self):
        print('parent\'s destructor', self)

    def displayEmployeeInfo(self):
        print("Name: %s Salary: %d Team: %s" % (self.name, self.salary, self.team))


def main():
    emp1 = HSBCEmployee("Pawan", 30000, "FI")
    emp1.displayEmployeeInfo()



if __name__ == '__main__':
    main()
