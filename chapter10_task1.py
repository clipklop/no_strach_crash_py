# ***
# An Employee class
# ***


class Employee():
    """ An employee class with its name and salary. """
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, adds_salary=5000):
        self.annual_salary += adds_salary


brown = Employee("Johnson", "Brown", 1000)
brown.give_raise()
brown.give_raise(101)
print(brown.annual_salary)