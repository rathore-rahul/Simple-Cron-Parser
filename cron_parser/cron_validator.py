from abc import abstractmethod, ABC

from cron_parser.constants import FieldValueRange
from cron_parser.exceptions import InvalidCronExpressionException


class CronValidator(ABC):
    @abstractmethod
    def validate(self, tokens):
        pass


class SimpleCronValidator(CronValidator):
    def validate(self, tokens):
        if  len(tokens) not in [len(FieldValueRange), len(FieldValueRange) + 1]:
            raise InvalidCronExpressionException("Invalid cron expression")
