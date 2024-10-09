from Employee import Employee

def test_give_default_raise():
    """Does method will add default value (5000) to the salary?"""
    my_employee=Employee('Micheal','Laron',30000)
    my_employee.give_raise()
    assert my_employee.annual_salary==35000

def test_give_custom_raise():
    """Does method will add custom value instead of 5000 to the salary?"""
    my_employee=Employee('Kate','Wilson',45000)
    my_employee.give_raise(3000)
    assert my_employee.annual_salary==48000
