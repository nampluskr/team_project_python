"""Field classes for Employee Management System."""
from __future__ import annotations
from enum import Enum
from typing import Optional


class TertiaryOptionEnum(Enum):
    NONE = 0
    G = 1    # >
    GE = 2   # >=
    S = 3    # <
    SE = 4   # <=


def tertiary_option_from_string(option: str) -> TertiaryOptionEnum:
    mapping = {
        "-g": TertiaryOptionEnum.G,
        "-ge": TertiaryOptionEnum.GE,
        "-s": TertiaryOptionEnum.S,
        "-se": TertiaryOptionEnum.SE,
    }
    if option in mapping:
        return mapping[option]
    return TertiaryOptionEnum.NONE


class Field:
    """Abstract base class for all fields."""

    def compare(self, other: "Field", subfield_index: int, tertiary_option: TertiaryOptionEnum) -> bool:
        raise NotImplementedError

    def equals(self, value: str) -> bool:
        raise NotImplementedError

    def compare_to(self, other: "Field") -> int:
        raise NotImplementedError

    def to_string(self) -> str:
        raise NotImplementedError

    @staticmethod
    def compare_string(first: str, second: str, opt: TertiaryOptionEnum) -> bool:
        if opt == TertiaryOptionEnum.G:
            return first > second
        elif opt == TertiaryOptionEnum.GE:
            return first >= second
        elif opt == TertiaryOptionEnum.NONE:
            return first == second
        elif opt == TertiaryOptionEnum.SE:
            return first <= second
        elif opt == TertiaryOptionEnum.S:
            return first < second
        return False

    @staticmethod
    def compare_int(first: int, second: int, opt: TertiaryOptionEnum) -> bool:
        if opt == TertiaryOptionEnum.G:
            return first > second
        elif opt == TertiaryOptionEnum.GE:
            return first >= second
        elif opt == TertiaryOptionEnum.NONE:
            return first == second
        elif opt == TertiaryOptionEnum.SE:
            return first <= second
        elif opt == TertiaryOptionEnum.S:
            return first < second
        return False


class EmployeeNumber(Field):
    def __init__(self, number: str):
        self._number = number
        self._year = number[:2]
        self._mod = number[2:]

    def get_year(self) -> int:
        return int(self._year)

    def get_mod(self) -> int:
        return int(self._mod)

    def to_string(self) -> str:
        return self._number

    def equals(self, value: str) -> bool:
        return self._number == value

    def compare(self, other: "Field", subfield_index: int, tertiary_option: TertiaryOptionEnum) -> bool:
        assert isinstance(other, EmployeeNumber)
        standard_year = other.get_year()
        standard_mod = other.get_mod()
        y = self.get_year()
        m = self.get_mod()

        if standard_year <= 19:
            standard_year += 100
        if y <= 19:
            y += 100

        if y == standard_year:
            return self.compare_int(m, standard_mod, tertiary_option)
        return self.compare_int(y, standard_year, tertiary_option)

    def compare_to(self, other: "Field") -> int:
        assert isinstance(other, EmployeeNumber)
        if self._number < other._number:
            return -1
        elif self._number > other._number:
            return 1
        return 0


class Name(Field):
    def __init__(self, full_name_or_first: str, second: Optional[str] = None):
        if second is not None:
            self._first = full_name_or_first
            self._second = second
        else:
            parts = full_name_or_first.split(" ", 1)
            if len(parts) != 2:
                raise ValueError(f"Invalid name format: {full_name_or_first}")
            self._first = parts[0]
            self._second = parts[1]

    @property
    def first(self) -> str:
        return self._first

    @property
    def second(self) -> str:
        return self._second

    def to_string(self) -> str:
        return f"{self._first} {self._second}"

    def equals(self, value: str) -> bool:
        other = Name(value)
        return self._first == other._first and self._second == other._second

    def compare(self, other: "Field", subfield_index: int, tertiary_option: TertiaryOptionEnum) -> bool:
        assert isinstance(other, Name)
        if subfield_index == 0:
            if self._first == other._first:
                return self.compare_string(self._second, other._second, tertiary_option)
            return self.compare_string(self._first, other._first, tertiary_option)
        elif subfield_index == 1:
            return self.compare_string(self._first, other._first, tertiary_option)
        elif subfield_index == 2:
            return self.compare_string(self._second, other._second, tertiary_option)
        raise ValueError(f"Subfield index out of bounds: {subfield_index}")

    def compare_to(self, other: "Field") -> int:
        assert isinstance(other, Name)
        if self._first == other._first:
            if self._second < other._second:
                return -1
            elif self._second > other._second:
                return 1
            return 0
        if self._first < other._first:
            return -1
        return 1


class CareerLevel(Field):
    def __init__(self, value: str):
        if len(value) != 3 or value[:2] != "CL" or value[2] not in "1234":
            raise ValueError(f"Invalid career level: {value}")
        self._value = value
        self._level_num = int(value[2])

    @property
    def level_num(self) -> int:
        return self._level_num

    def to_string(self) -> str:
        return self._value

    def equals(self, value: str) -> bool:
        return self._value == value

    def compare(self, other: "Field", subfield_index: int, tertiary_option: TertiaryOptionEnum) -> bool:
        assert isinstance(other, CareerLevel)
        return self.compare_int(self._level_num, other._level_num, tertiary_option)

    def compare_to(self, other: "Field") -> int:
        assert isinstance(other, CareerLevel)
        return self._level_num - other._level_num


class PhoneNumber(Field):
    def __init__(self, phone_number: str):
        self._phone_number = phone_number
        parts = phone_number.split("-")
        if len(parts) != 3:
            raise ValueError(f"Invalid PhoneNumber format: {phone_number}")
        self._first = parts[0]
        self._middle = parts[1]
        self._last = parts[2]

    @property
    def first(self) -> str:
        return self._first

    @property
    def middle(self) -> str:
        return self._middle

    @property
    def last(self) -> str:
        return self._last

    def to_string(self) -> str:
        return f"{self._first}-{self._middle}-{self._last}"

    def equals(self, value: str) -> bool:
        other = PhoneNumber(value)
        return self._first == other._first and self._middle == other._middle and self._last == other._last

    def compare(self, other: "Field", subfield_index: int, tertiary_option: TertiaryOptionEnum) -> bool:
        assert isinstance(other, PhoneNumber)
        if subfield_index == 2:
            return self.compare_string(self._middle, other._middle, tertiary_option)
        elif subfield_index == 3:
            return self.compare_string(self._last, other._last, tertiary_option)
        return self.compare_string(self._phone_number, other._phone_number, tertiary_option)

    def compare_to(self, other: "Field") -> int:
        assert isinstance(other, PhoneNumber)
        if self._phone_number < other._phone_number:
            return -1
        elif self._phone_number > other._phone_number:
            return 1
        return 0


class Birthday(Field):
    def __init__(self, birthday_or_year, month: Optional[int] = None, day: Optional[int] = None):
        if month is not None and day is not None:
            self._year = birthday_or_year
            self._month = month
            self._day = day
        else:
            s = str(birthday_or_year)
            if len(s) != 8:
                raise ValueError(f"Invalid birthday format: {s}")
            self._year = int(s[0:4])
            self._month = int(s[4:6])
            self._day = int(s[6:8])

    @property
    def year(self) -> int:
        return self._year

    @property
    def month(self) -> int:
        return self._month

    @property
    def day(self) -> int:
        return self._day

    def _to_int(self) -> int:
        return self._year * 10000 + self._month * 100 + self._day

    def to_string(self) -> str:
        return f"{self._year:04d}{self._month:02d}{self._day:02d}"

    def equals(self, value: str) -> bool:
        return self.to_string() == value

    def compare(self, other: "Field", subfield_index: int, tertiary_option: TertiaryOptionEnum) -> bool:
        assert isinstance(other, Birthday)
        if subfield_index == 0:
            return self.compare_int(self._to_int(), other._to_int(), tertiary_option)
        elif subfield_index == 1:
            return self.compare_int(self._year, other._year, tertiary_option)
        elif subfield_index == 2:
            return self.compare_int(self._month, other._month, tertiary_option)
        elif subfield_index == 3:
            return self.compare_int(self._day, other._day, tertiary_option)
        raise ValueError(f"Invalid subfieldIndex: {subfield_index}")

    def compare_to(self, other: "Field") -> int:
        assert isinstance(other, Birthday)
        if self._year != other._year:
            return self._year - other._year
        if self._month != other._month:
            return self._month - other._month
        return self._day - other._day


class Certi(Field):
    def __init__(self, certi: str):
        self._certi = certi

    def get_certi_level(self) -> int:
        levels = {"ADV": 0, "PRO": 1, "EX": 2}
        if self._certi not in levels:
            raise ValueError(f"Invalid certi: {self._certi}")
        return levels[self._certi]

    def to_string(self) -> str:
        return self._certi

    def equals(self, value: str) -> bool:
        return self._certi == value

    def compare(self, other: "Field", subfield_index: int, tertiary_option: TertiaryOptionEnum) -> bool:
        assert isinstance(other, Certi)
        return self.compare_int(self.get_certi_level(), other.get_certi_level(), tertiary_option)

    def compare_to(self, other: "Field") -> int:
        assert isinstance(other, Certi)
        a = self.get_certi_level()
        b = other.get_certi_level()
        if a == b:
            return 0
        return 1 if a > b else -1
