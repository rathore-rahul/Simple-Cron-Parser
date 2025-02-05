from abc import abstractmethod, ABC

from cron_parser.constants import FieldValueRange, FieldToDisplayName
from cron_parser.cron_field import CronField


class CronParser(ABC):
    @abstractmethod
    def parse(self, tokens):
        pass


class SimpleCronParser(CronParser):
    def parse(self, tokens):
        result = {}
        result["command"] = tokens[-1]
        tokens.pop()
        enum_list = list(FieldValueRange)
        for index, token in enumerate(tokens):
            field = enum_list[index]
            cron_field = CronField(field, token)
            result[FieldToDisplayName[field.name].value] = cron_field.generate_cron_values()
        return result