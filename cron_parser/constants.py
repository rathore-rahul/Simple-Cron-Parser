from enum import Enum


class FieldValueRange(Enum):
    # this is the order of the field in cron schedule. Keeping it same as in cron expression
    # if a new field need to be added. add it here to maintain the order. this is the only place that need to be changed
    MINUTE = (0, 59)
    HOUR = (0, 23)
    DAY_OF_MONTH = (1, 31)
    MONTH = (1, 12)
    DAY_OF_WEEK = (1, 7)
    YEAR = (2025, 3000)


class FieldToDisplayName(Enum):
    MINUTE = "minute"
    HOUR = "hour"
    DAY_OF_MONTH = "day of month"
    MONTH = "month"
    DAY_OF_WEEK = "day of week"
    YEAR = "year"