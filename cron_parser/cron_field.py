from cron_parser.constants import FieldValueRange
from cron_parser.token_factory import TokenFactory

class CronField:
    def __init__(self, field: FieldValueRange , token: str) -> None:
        self.field = field
        self.token = token

    def generate_cron_values(self):
        token = TokenFactory.create_token(self.field, self.token)
        return token.parse_token_values()
