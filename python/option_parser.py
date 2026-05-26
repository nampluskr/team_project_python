"""Option parsing utilities for Employee Management System."""
from typing import List

from enums import (
    FieldEnum,
    PrimaryOptionEnum,
    SecondaryOptionEnum,
    primary_option_from_string,
    secondary_option_from_string,
)
from field import TertiaryOptionEnum, tertiary_option_from_string


class OptionParser:
    def __init__(self, options: List[str]):
        self.primary_option = PrimaryOptionEnum.NONE
        self.secondary_option = SecondaryOptionEnum.NONE
        self.tertiary_option = TertiaryOptionEnum.NONE

        if not options:
            return

        if len(options) == 3:
            if options[0]:
                self.primary_option = primary_option_from_string(options[0])
            if options[1]:
                self.secondary_option = secondary_option_from_string(options[1])
            if options[2]:
                self.tertiary_option = tertiary_option_from_string(options[2])
        elif len(options) == 2:
            if options[0]:
                self.secondary_option = secondary_option_from_string(options[0])
            if options[1]:
                self.tertiary_option = tertiary_option_from_string(options[1])


def get_field_index_from_option(option_parser: OptionParser, input_field_enum: FieldEnum) -> int:
    secondary_option = option_parser.secondary_option
    field_index = 0

    if secondary_option == SecondaryOptionEnum.F:
        field_index = 1
    elif secondary_option == SecondaryOptionEnum.M:
        if input_field_enum == FieldEnum.FIELD_PHONE_NUMBER:
            field_index = 2
        elif input_field_enum == FieldEnum.FIELD_BIRTH_DAY:
            field_index = 2
    elif secondary_option == SecondaryOptionEnum.L:
        if input_field_enum == FieldEnum.FIELD_PHONE_NUMBER:
            field_index = 3
        elif input_field_enum == FieldEnum.FIELD_NAME:
            field_index = 2
    elif secondary_option == SecondaryOptionEnum.Y:
        if input_field_enum == FieldEnum.FIELD_BIRTH_DAY:
            field_index = 1
    elif secondary_option == SecondaryOptionEnum.D:
        if input_field_enum == FieldEnum.FIELD_BIRTH_DAY:
            field_index = 3

    return field_index
