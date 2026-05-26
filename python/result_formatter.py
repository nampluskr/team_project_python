"""Result string formatting utilities."""
from typing import List

from employee import Employee


YEAR_1990_EMPLOYEE_NUMBER = 90000000
YEAR_PREFIX_19 = 1900000000
YEAR_PREFIX_20 = 2000000000


def _get_employee_number_sort_key(employee_number: int) -> int:
    if employee_number >= YEAR_1990_EMPLOYEE_NUMBER:
        return YEAR_PREFIX_19 + employee_number
    return YEAR_PREFIX_20 + employee_number


def _format_employee(command_type: str, employee: Employee) -> str:
    return ",".join([
        command_type,
        employee.employee_number.to_string(),
        employee.name.to_string(),
        employee.career_level.to_string(),
        employee.phone_number.to_string(),
        employee.birthday.to_string(),
        employee.certi.to_string(),
    ])


def format_employee_list_with_print(employee_list: List[Employee],
                                     command_type: str, count: int) -> List[str]:
    """Format with -p option (print up to `count` records)."""
    if not employee_list:
        return [f"{command_type},NONE"]

    sorted_list = sorted(
        employee_list,
        key=lambda e: _get_employee_number_sort_key(int(e.employee_number.to_string()))
    )

    result = []
    limit = min(count, len(sorted_list))
    for i in range(limit):
        result.append(_format_employee(command_type, sorted_list[i]))
    return result


def format_employee_list_count(employee_list: List[Employee],
                                command_type: str) -> List[str]:
    """Format without -p option (just count)."""
    if not employee_list:
        return [f"{command_type},NONE"]
    return [f"{command_type},{len(employee_list)}"]
