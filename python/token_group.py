"""TokenGroup class for parsed command tokens."""
from typing import List

from enums import CombinationEnum, combination_from_string


class TokenGroup:
    def __init__(self, cmd_type: str,
                 first_options: List[str], first_params: List[str],
                 combination: str = " ",
                 second_options: List[str] = None,
                 second_params: List[str] = None):
        self.type = cmd_type
        self.first_options = first_options
        self.first_params = first_params
        self.combination = combination
        self.second_options = second_options or []
        self.second_params = second_params or []

    @property
    def combination_enum(self) -> CombinationEnum:
        return combination_from_string(self.combination)
