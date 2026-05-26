"""Employee class for Employee Management System."""
from field import EmployeeNumber, Name, CareerLevel, PhoneNumber, Birthday, Certi


class Employee:
    def __init__(self, employee_number: str, name: str, career_level: str,
                 phone_number: str, birthday: str, certi: str):
        self.employee_number = EmployeeNumber(employee_number)
        self.name = Name(name)
        self.career_level = CareerLevel(career_level)
        self.phone_number = PhoneNumber(phone_number)
        self.birthday = Birthday(birthday)
        self.certi = Certi(certi)

    def copy(self) -> "Employee":
        return Employee(
            self.employee_number.to_string(),
            self.name.to_string(),
            self.career_level.to_string(),
            self.phone_number.to_string(),
            self.birthday.to_string(),
            self.certi.to_string(),
        )

    def __eq__(self, other) -> bool:
        if not isinstance(other, Employee):
            return False
        return self.employee_number.to_string() == other.employee_number.to_string()

    def __hash__(self) -> int:
        return hash(self.employee_number.to_string())
