class Employee:
    number_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

        Employee.number_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

if __name__ == '__main__':
    print('Employee.number_of_employees:', Employee.number_of_employees)
    emp_1 = Employee('Corey', 'Schafer', 50_000)
    emp_2 = Employee('Test', 'Employee', 60_000)
    print('Employee.number_of_employees post making emp_1 and emp_2:', Employee.number_of_employees)

    print('emp_1.pay:', emp_1.pay)
    emp_1.apply_raise()
    print('emp_1.pay - post emp_1.apply_raise():', emp_1.pay)

    print('Employee.raise_amount:', Employee.raise_amount)
    print('emp_1.raise_amount:', emp_1.raise_amount)
    print('emp_2.raise_amount:', emp_2.raise_amount)

    print('\nsetting emp_1.raise_amount = 1.05')
    emp_1.raise_amount = 1.05

    print('Employee.raise_amount:', Employee.raise_amount)
    print('emp_1.raise_amount:', emp_1.raise_amount)
    print('emp_2.raise_amount:', emp_2.raise_amount)

    print('Employee.__dict__:', Employee.__dict__)
    print('emp_1.__dict__:', emp_1.__dict__)
