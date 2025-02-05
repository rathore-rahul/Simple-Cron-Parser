from cron_parser.constants import FieldValueRange
from cron_parser.tokens import Token, WildcardToken, StepRangeToken, RangeToken, CommaToken, ValueToken


class TokenFactory:
    @staticmethod
    def create_token(field: FieldValueRange, token: str) -> Token:
        """Factory method to create appropriate token based on cron expression."""
        if token == '*':
            return WildcardToken(field, token)
        elif '/' in token:
            return StepRangeToken(field, token)
        elif '-' in token:
            return RangeToken(field, token)
        elif ',' in token:
            return CommaToken(field, token)
        else:
            return ValueToken(field, token)
