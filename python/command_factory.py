"""Command factory - builds Command objects from TokenGroups."""
from typing import Tuple

from commands import (
    Command, AddCommand, DeleteCommand, SearchCommand, ModCommand, CountCommand,
    CMD_ADD, CMD_DEL, CMD_SCH, CMD_CNT, CMD_MOD,
)
from employee import Employee
from employee_store import EmployeeStore
from enums import CombinationEnum, get_secondary_option_type
from option_parser import OptionParser
from token_group import TokenGroup


FIELD_MAP = {
    "employeeNum": "employeeNumber",
    "name": "name",
    "cl": "careerLevel",
    "phoneNum": "phoneNumber",
    "birthday": "birthDay",
    "certi": "certi",
}


def _get_condition_pair(params: list, option_parser: OptionParser) -> Tuple[str, str]:
    """Build condition pair from params, handling secondary option subfield encoding."""
    field_name = FIELD_MAP.get(params[0])
    if field_name is None:
        raise ValueError(f"Wrong field: {params[0]}")

    sec_type = get_secondary_option_type(option_parser.secondary_option)

    if sec_type == 1:  # -f (first name)
        return (field_name, params[1] + " KIM")
    if sec_type == 2:  # -l (last name / phone last)
        if field_name == "name":
            return (field_name, "HOHAN " + params[1])
        if field_name == "phoneNumber":
            return (field_name, "010-0000-" + params[1])
    if sec_type == 3:  # -m (phone middle / birthday month)
        if field_name == "birthDay":
            return (field_name, "9999" + params[1] + "99")
        if field_name == "phoneNumber":
            return (field_name, "010-" + params[1] + "-0000")
    if sec_type == 4:  # -y (birthday year)
        return (field_name, params[1] + "9999")
    if sec_type == 5:  # -d (birthday day)
        return (field_name, "999999" + params[1])

    return (field_name, params[1])


def _get_modify_pair(params: list, option_parser: OptionParser) -> Tuple[str, str]:
    """Build modify condition pair from params[2], params[3]."""
    field_name = FIELD_MAP.get(params[2])
    if field_name is None or field_name == "employeeNumber":
        raise ValueError(f"Wrong field: {params[2]}")
    return (field_name, params[3])


def build_command(tokens: TokenGroup) -> Command:
    """Build a Command from a TokenGroup."""
    if tokens.combination_enum == CombinationEnum.NONE:
        return _build_single_command(tokens.type, tokens.first_options, tokens.first_params)
    return _build_and_or_command(tokens)


def _build_single_command(cmd: str, options: list, params: list) -> Command:
    option_parser = OptionParser(options)

    if cmd == CMD_ADD:
        employee = Employee(params[0], params[1], params[2], params[3], params[4], params[5])
        return AddCommand(option_parser, employee)
    if cmd == CMD_DEL:
        return DeleteCommand(option_parser, _get_condition_pair(params, option_parser))
    if cmd == CMD_MOD:
        return ModCommand(
            option_parser,
            _get_condition_pair(params, option_parser),
            _get_modify_pair(params, option_parser),
        )
    if cmd == CMD_SCH:
        return SearchCommand(option_parser, _get_condition_pair(params, option_parser))
    if cmd == CMD_CNT:
        return CountCommand()
    raise ValueError(f"Wrong command: {cmd}")


def _build_and_or_command(tokens: TokenGroup) -> Command:
    cmd = tokens.type
    first_params = tokens.first_params
    second_params = tokens.second_params
    combination = tokens.combination_enum
    first_options = tokens.first_options
    second_options = tokens.second_options

    first_option_parser = OptionParser(first_options)
    second_option_parser = OptionParser(second_options)

    if cmd == CMD_ADD:
        raise ValueError("And Or Line must not have ADD.")
    if cmd == CMD_DEL:
        return DeleteCommand(
            first_option_parser,
            _get_condition_pair(first_params, first_option_parser),
            combination,
            second_option_parser,
            _get_condition_pair(second_params, second_option_parser),
        )
    if cmd == CMD_MOD:
        return ModCommand(
            first_option_parser,
            _get_condition_pair(first_params, first_option_parser),
            _get_modify_pair(second_params, second_option_parser),
            combination,
            second_option_parser,
            _get_condition_pair(second_params, second_option_parser),
        )
    if cmd == CMD_SCH:
        return SearchCommand(
            first_option_parser,
            _get_condition_pair(first_params, first_option_parser),
            combination,
            second_option_parser,
            _get_condition_pair(second_params, second_option_parser),
        )
    if cmd == CMD_CNT:
        return CountCommand()
    raise ValueError(f"Wrong command: {cmd}")
