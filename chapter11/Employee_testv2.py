from Employee import Employee
import pytest

@pytest.fixture
def my_employee():
    """Create instance from the Employee Class"""
    employee=Employee('Martin','Donald',45000)
    return employee

def test_give_default_raise(my_employee):
    """Does method will add default value (5000) to the salary?"""
    my_employee.give_raise()
    assert my_employee.annual_salary==50000

def test_give_custom_raise(my_employee):
    """Does method will add custom value instead of 5000 to the salary?"""
    my_employee.give_raise(3000)
    assert my_employee.annual_salary==48000
