from __future__ import annotations

from abc import ABC, abstractmethod

from cron_parser.exceptions import InvalidCronExpressionException


class Token(ABC):
    def __init__(self, field, token) -> None:
        self.field = field
        self.token = token

    def _validate(self, result) -> None:
        value_range = self.field.value
        for item in result:
            if value_range[0] <= item <= value_range[1]:
                continue
            else:
                raise InvalidCronExpressionException(f'{self.field.name} Value {item} out of range {value_range}')

    @abstractmethod
    def _generate_values(self):
        pass

    def parse_token_values(self):
        values = self._generate_values()
        self._validate(values)
        return values



class WildcardToken(Token):
    def _generate_values(self):
        return list(range(self.field.value[0], self.field.value[1]+1))


class CommaToken(Token):
    def _generate_values(self):
        return [int(value) for value in self.token.split(',')]


class RangeToken(Token):
    def _generate_values(self):
        start, end = self.token.split('-')
        return list(range(int(start), int(end) + 1))


class StepRangeToken(Token):
    def _get_range_and_step(self):
        range_token, step = self.token.split('/')
        step = int(step)
        if range_token == '*':
            start, end = self.field.value
        elif '-' in range_token:
            start, end = range_token.split('-')
            start = int(start)
            end = int(end)
        else:
            start = int(range_token)
            end = self.field.value[1]
        return start, end, step

    def _generate_values(self):
        start, end, step = self._get_range_and_step()
        return list(range(start, end + 1, step))

class ValueToken(Token):
    def _generate_values(self):
        return [int(self.token)]