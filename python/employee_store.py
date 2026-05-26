"""Employee Store implementation for Employee Management System."""
from typing import List, Callable, Dict

from employee import Employee
from enums import FieldEnum, CombinationEnum
from field import (
    Field, TertiaryOptionEnum, EmployeeNumber, Name,
    CareerLevel, PhoneNumber, Birthday, Certi,
)


class EmployeeStore:
    def __init__(self):
        self._employees: List[Employee] = []
        self._field_creators: Dict[FieldEnum, Callable[[str], Field]] = {
            FieldEnum.FIELD_EMPLOYEE_NUMBER: lambda v: EmployeeNumber(v),
            FieldEnum.FIELD_NAME: lambda v: Name(v),
            FieldEnum.FIELD_CAREER_LEVEL: lambda v: CareerLevel(v),
            FieldEnum.FIELD_PHONE_NUMBER: lambda v: PhoneNumber(v),
            FieldEnum.FIELD_BIRTH_DAY: lambda v: Birthday(v),
            FieldEnum.FIELD_CERTI: lambda v: Certi(v),
        }
        self._field_extractors: Dict[FieldEnum, Callable[[Employee], Field]] = {
            FieldEnum.FIELD_EMPLOYEE_NUMBER: lambda e: e.employee_number,
            FieldEnum.FIELD_NAME: lambda e: e.name,
            FieldEnum.FIELD_CAREER_LEVEL: lambda e: e.career_level,
            FieldEnum.FIELD_PHONE_NUMBER: lambda e: e.phone_number,
            FieldEnum.FIELD_BIRTH_DAY: lambda e: e.birthday,
            FieldEnum.FIELD_CERTI: lambda e: e.certi,
        }

    def add(self, employee: Employee) -> None:
        self._employees.append(employee)

    def count(self) -> int:
        return len(self._employees)

    def search(self, field: FieldEnum, value: str,
               tertiary_option: TertiaryOptionEnum,
               subfield_index: int = 0) -> List[Employee]:
        creator = self._field_creators.get(field)
        extractor = self._field_extractors.get(field)
        if creator is None or extractor is None:
            return []

        search_field = creator(value)
        result = []
        for emp in self._employees:
            target_field = extractor(emp)
            if target_field.compare(search_field, subfield_index, tertiary_option):
                result.append(emp)
        return result

    def search_and_or(self, field1: FieldEnum, value1: str,
                      tertiary1: TertiaryOptionEnum, subfield_index1: int,
                      combination: CombinationEnum,
                      field2: FieldEnum, value2: str,
                      tertiary2: TertiaryOptionEnum, subfield_index2: int) -> List[Employee]:
        search_field1 = self._field_creators[field1](value1)
        search_field2 = self._field_creators[field2](value2)

        result = []
        for emp in self._employees:
            target1 = self._field_extractors[field1](emp)
            target2 = self._field_extractors[field2](emp)
            match1 = target1.compare(search_field1, subfield_index1, tertiary1)
            match2 = target2.compare(search_field2, subfield_index2, tertiary2)

            if combination == CombinationEnum.OR:
                if match1 or match2:
                    result.append(emp)
            else:
                if match1 and match2:
                    result.append(emp)
        return result

    def delete(self, field: FieldEnum, value: str,
               subfield_index: int = 0) -> List[Employee]:
        searched = self.search(field, value, TertiaryOptionEnum.NONE, subfield_index)
        self._employees = [e for e in self._employees if e not in searched]
        return searched

    def delete_and_or(self, field1: FieldEnum, value1: str, subfield_index1: int,
                      combination: CombinationEnum,
                      field2: FieldEnum, value2: str, subfield_index2: int) -> List[Employee]:
        searched = self.search_and_or(
            field1, value1, TertiaryOptionEnum.NONE, subfield_index1,
            combination,
            field2, value2, TertiaryOptionEnum.NONE, subfield_index2,
        )
        self._employees = [e for e in self._employees if e not in searched]
        return searched

    def modify(self, field: FieldEnum, value: str,
               modify_field: FieldEnum, modify_value: str,
               subfield_index: int = 0) -> List[Employee]:
        if modify_field == FieldEnum.FIELD_EMPLOYEE_NUMBER:
            raise ValueError("Employee number cannot be modified")

        searched = self.search(field, value, TertiaryOptionEnum.NONE, subfield_index)
        self._employees = [e for e in self._employees if e not in searched]

        modified = self._modify_field_of_list(modify_field, modify_value, searched)
        self._employees.extend(modified)
        return searched

    def modify_and_or(self, field1: FieldEnum, value1: str, subfield_index1: int,
                      combination: CombinationEnum,
                      field2: FieldEnum, value2: str, subfield_index2: int,
                      modify_field: FieldEnum, modify_value: str) -> List[Employee]:
        if modify_field == FieldEnum.FIELD_EMPLOYEE_NUMBER:
            raise ValueError("Employee number cannot be modified")

        searched = self.search_and_or(
            field1, value1, TertiaryOptionEnum.NONE, subfield_index1,
            combination,
            field2, value2, TertiaryOptionEnum.NONE, subfield_index2,
        )
        self._employees = [e for e in self._employees if e not in searched]

        modified = self._modify_field_of_list(modify_field, modify_value, searched)
        self._employees.extend(modified)
        return searched

    @staticmethod
    def _modify_field_of_list(modify_field: FieldEnum, modify_value: str,
                              employees: List[Employee]) -> List[Employee]:
        result = []
        for emp in employees:
            copy = emp.copy()
            if modify_field == FieldEnum.FIELD_EMPLOYEE_NUMBER:
                copy.employee_number = EmployeeNumber(modify_value)
            elif modify_field == FieldEnum.FIELD_NAME:
                copy.name = Name(modify_value)
            elif modify_field == FieldEnum.FIELD_CAREER_LEVEL:
                copy.career_level = CareerLevel(modify_value)
            elif modify_field == FieldEnum.FIELD_PHONE_NUMBER:
                copy.phone_number = PhoneNumber(modify_value)
            elif modify_field == FieldEnum.FIELD_BIRTH_DAY:
                copy.birthday = Birthday(modify_value)
            elif modify_field == FieldEnum.FIELD_CERTI:
                copy.certi = Certi(modify_value)
            result.append(copy)
        return result
