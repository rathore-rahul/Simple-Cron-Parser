class CronParserService:
    def __init__(self, cron_expression, tokenizer, validator, parser):
        self.tokenizer = tokenizer
        self.validator = validator
        self.parser = parser
        self.cron_expression = cron_expression

    def parse(self):
        tokens = self.tokenizer.tokenize(self.cron_expression)
        self.validator.validate(tokens)
        return self.parser.parse(tokens)

    @staticmethod
    def format_output(fields_map):
        return '\n'.join(
            f'{field:<14} {values if field == "command" else " ".join(map(str, values))}'
            for field, values in fields_map.items()
        )
