"""Enums for Employee Management System."""
from enum import Enum


class FieldEnum(Enum):
    FIELD_EMPLOYEE_NUMBER = "employeeNumber"
    FIELD_NAME = "name"
    FIELD_FIRST_NAME = "nameFirst"
    FIELD_SECOND_NAME = "nameSecond"
    FIELD_CAREER_LEVEL = "careerLevel"
    FIELD_PHONE_NUMBER = "phoneNumber"
    FIELD_PHONE_NUMBER_MIDDLE = "phoneNumberMiddle"
    FIELD_PHONE_NUMBER_LAST = "phoneNumberLast"
    FIELD_BIRTH_DAY = "birthDay"
    FIELD_BIRTH_DAY_YEAR = "birthDayYear"
    FIELD_BIRTH_DAY_MONTH = "birthDayMonth"
    FIELD_BIRTH_DAY_DAY = "birthDayDay"
    FIELD_CERTI = "certi"


def field_enum_from_string(field: str) -> FieldEnum:
    for e in FieldEnum:
        if e.value == field:
            return e
    raise ValueError(f"Invalid field name: {field}")


class CombinationEnum(Enum):
    NONE = 0
    OR = 1
    AND = 2


def combination_from_string(s: str) -> CombinationEnum:
    if s == "-a":
        return CombinationEnum.AND
    if s == "-o":
        return CombinationEnum.OR
    return CombinationEnum.NONE


class PrimaryOptionEnum(Enum):
    NONE = 0
    PRINT = 1


def primary_option_from_string(option: str) -> PrimaryOptionEnum:
    if option == "-p":
        return PrimaryOptionEnum.PRINT
    if option in (" ", ""):
        return PrimaryOptionEnum.NONE
    raise ValueError(f"Invalid primary option: {option}")


class SecondaryOptionEnum(Enum):
    NONE = 0
    F = 1
    L = 2
    M = 3
    Y = 4
    D = 5


def secondary_option_from_string(option: str) -> SecondaryOptionEnum:
    mapping = {
        "-f": SecondaryOptionEnum.F,
        "-l": SecondaryOptionEnum.L,
        "-m": SecondaryOptionEnum.M,
        "-y": SecondaryOptionEnum.Y,
        "-d": SecondaryOptionEnum.D,
    }
    if option in mapping:
        return mapping[option]
    if option in (" ", ""):
        return SecondaryOptionEnum.NONE
    raise ValueError(f"Invalid secondary option: {option}")


def get_secondary_option_type(opt: SecondaryOptionEnum) -> int:
    return opt.value
