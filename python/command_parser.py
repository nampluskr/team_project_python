"""Command parser - parses input lines into TokenGroups."""
from typing import List

from token_group import TokenGroup


class CommandParser:
    def parse(self, line: str) -> TokenGroup:
        tokens = line.split(",")

        cmd_type = tokens[0]
        options = tokens[1:4]
        params = tokens[4:]

        # Check for AND/OR condition
        condition_idx = self._get_condition_index(params)
        if condition_idx != -1:
            condition = params[condition_idx]
            first_params = params[:condition_idx]
            second_options = [" ", params[condition_idx + 1], params[condition_idx + 2]]
            second_params = params[condition_idx + 3:]

            return TokenGroup(
                cmd_type,
                self._get_valid_list(options),
                self._get_valid_list(first_params),
                condition,
                self._get_valid_list(second_options),
                self._get_valid_list(second_params),
            )

        return TokenGroup(cmd_type, self._get_valid_list(options), self._get_valid_list(params))

    @staticmethod
    def _get_condition_index(params: List[str]) -> int:
        for i, p in enumerate(params):
            if p == "-a" or p == "-o":
                return i
        return -1

    @staticmethod
    def _get_valid_list(lst: List[str]) -> List[str]:
        return [item for item in lst if item.strip()]
