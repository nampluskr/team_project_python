"""Command classes for Employee Management System."""
from typing import List

from employee import Employee
from employee_store import EmployeeStore
from enums import (
    CombinationEnum, FieldEnum, PrimaryOptionEnum,
    field_enum_from_string,
)
from option_parser import OptionParser, get_field_index_from_option
from result_formatter import format_employee_list_with_print, format_employee_list_count

MAX_RESULT_NUMBER = 5

CMD_ADD = "ADD"
CMD_DEL = "DEL"
CMD_SCH = "SCH"
CMD_CNT = "CNT"
CMD_MOD = "MOD"


class Command:
    """Base command class."""

    def __init__(self, first_option_parser: OptionParser = None,
                 first_condition_pair: tuple = None,
                 combination_enum: CombinationEnum = CombinationEnum.NONE,
                 second_option_parser: OptionParser = None,
                 second_condition_pair: tuple = None):
        self.first_option_parser = first_option_parser
        self.first_condition_pair = first_condition_pair or ("", "")
        self.combination_enum = combination_enum
        self.second_option_parser = second_option_parser or OptionParser([" ", " "])
        self.second_condition_pair = second_condition_pair or (" ", " ")

    def execute(self, store: EmployeeStore) -> List[str]:
        if self.combination_enum in (CombinationEnum.AND, CombinationEnum.OR):
            return self.execute_and_or(store)
        return self.execute_single(store)

    def execute_single(self, store: EmployeeStore) -> List[str]:
        return []

    def execute_and_or(self, store: EmployeeStore) -> List[str]:
        return []


class AddCommand(Command):
    def __init__(self, option_parser: OptionParser, employee: Employee):
        super().__init__(first_option_parser=option_parser)
        self._employee = employee

    def execute(self, store: EmployeeStore) -> List[str]:
        store.add(self._employee)
        return []


class DeleteCommand(Command):
    def __init__(self, first_option_parser: OptionParser,
                 first_condition_pair: tuple,
                 combination_enum: CombinationEnum = CombinationEnum.NONE,
                 second_option_parser: OptionParser = None,
                 second_condition_pair: tuple = None):
        super().__init__(first_option_parser, first_condition_pair,
                         combination_enum, second_option_parser, second_condition_pair)

    def execute_single(self, store: EmployeeStore) -> List[str]:
        field_condition = field_enum_from_string(self.first_condition_pair[0])
        field_index = get_field_index_from_option(self.first_option_parser, field_condition)

        employee_list = store.delete(field_condition, self.first_condition_pair[1], field_index)

        if self.first_option_parser.primary_option == PrimaryOptionEnum.PRINT:
            return format_employee_list_with_print(employee_list, CMD_DEL, MAX_RESULT_NUMBER)
        return format_employee_list_count(employee_list, CMD_DEL)

    def execute_and_or(self, store: EmployeeStore) -> List[str]:
        first_field = field_enum_from_string(self.first_condition_pair[0])
        second_field = field_enum_from_string(self.second_condition_pair[0])
        first_index = get_field_index_from_option(self.first_option_parser, first_field)
        second_index = get_field_index_from_option(self.second_option_parser, second_field)

        employee_list = store.delete_and_or(
            first_field, self.first_condition_pair[1], first_index,
            self.combination_enum,
            second_field, self.second_condition_pair[1], second_index,
        )

        if self.first_option_parser.primary_option == PrimaryOptionEnum.PRINT:
            return format_employee_list_with_print(employee_list, CMD_DEL, MAX_RESULT_NUMBER)
        return format_employee_list_count(employee_list, CMD_DEL)


class SearchCommand(Command):
    def __init__(self, first_option_parser: OptionParser,
                 first_condition_pair: tuple,
                 combination_enum: CombinationEnum = CombinationEnum.NONE,
                 second_option_parser: OptionParser = None,
                 second_condition_pair: tuple = None):
        super().__init__(first_option_parser, first_condition_pair,
                         combination_enum, second_option_parser, second_condition_pair)

    def execute_single(self, store: EmployeeStore) -> List[str]:
        field_condition = field_enum_from_string(self.first_condition_pair[0])
        field_index = get_field_index_from_option(self.first_option_parser, field_condition)
        tertiary_option = self.first_option_parser.tertiary_option

        employee_list = store.search(field_condition, self.first_condition_pair[1],
                                     tertiary_option, field_index)

        if self.first_option_parser.primary_option == PrimaryOptionEnum.PRINT:
            return format_employee_list_with_print(employee_list, CMD_SCH, MAX_RESULT_NUMBER)
        return format_employee_list_count(employee_list, CMD_SCH)

    def execute_and_or(self, store: EmployeeStore) -> List[str]:
        first_field = field_enum_from_string(self.first_condition_pair[0])
        second_field = field_enum_from_string(self.second_condition_pair[0])
        first_index = get_field_index_from_option(self.first_option_parser, first_field)
        second_index = get_field_index_from_option(self.second_option_parser, second_field)
        first_tertiary = self.first_option_parser.tertiary_option
        second_tertiary = self.second_option_parser.tertiary_option

        employee_list = store.search_and_or(
            first_field, self.first_condition_pair[1], first_tertiary, first_index,
            self.combination_enum,
            second_field, self.second_condition_pair[1], second_tertiary, second_index,
        )

        if self.first_option_parser.primary_option == PrimaryOptionEnum.PRINT:
            return format_employee_list_with_print(employee_list, CMD_SCH, MAX_RESULT_NUMBER)
        return format_employee_list_count(employee_list, CMD_SCH)


class ModCommand(Command):
    def __init__(self, first_option_parser: OptionParser,
                 first_condition_pair: tuple,
                 condition_modify_pair: tuple,
                 combination_enum: CombinationEnum = CombinationEnum.NONE,
                 second_option_parser: OptionParser = None,
                 second_condition_pair: tuple = None):
        super().__init__(first_option_parser, first_condition_pair,
                         combination_enum, second_option_parser, second_condition_pair)
        self._condition_modify_pair = condition_modify_pair

    def execute_single(self, store: EmployeeStore) -> List[str]:
        field_condition = field_enum_from_string(self.first_condition_pair[0])
        field_modify_condition = field_enum_from_string(self._condition_modify_pair[0])
        field_index = get_field_index_from_option(self.first_option_parser, field_condition)

        employee_list = store.modify(
            field_condition, self.first_condition_pair[1],
            field_modify_condition, self._condition_modify_pair[1],
            field_index,
        )

        if self.first_option_parser.primary_option == PrimaryOptionEnum.PRINT:
            return format_employee_list_with_print(employee_list, CMD_MOD, MAX_RESULT_NUMBER)
        return format_employee_list_count(employee_list, CMD_MOD)

    def execute_and_or(self, store: EmployeeStore) -> List[str]:
        first_field = field_enum_from_string(self.first_condition_pair[0])
        second_field = field_enum_from_string(self.second_condition_pair[0])
        field_modify_condition = field_enum_from_string(self._condition_modify_pair[0])
        first_index = get_field_index_from_option(self.first_option_parser, first_field)
        second_index = get_field_index_from_option(self.second_option_parser, second_field)

        employee_list = store.modify_and_or(
            first_field, self.first_condition_pair[1], first_index,
            self.combination_enum,
            second_field, self.second_condition_pair[1], second_index,
            field_modify_condition, self._condition_modify_pair[1],
        )

        if self.first_option_parser.primary_option == PrimaryOptionEnum.PRINT:
            return format_employee_list_with_print(employee_list, CMD_MOD, MAX_RESULT_NUMBER)
        return format_employee_list_count(employee_list, CMD_MOD)


class CountCommand(Command):
    def execute(self, store: EmployeeStore) -> List[str]:
        return [f"{CMD_CNT},{store.count()}"]
