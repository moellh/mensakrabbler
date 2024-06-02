# imports

from enum import Enum


class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4

    # use Weekday(i) to get Enum element
    # use WEEKDAY.value to get integer value
