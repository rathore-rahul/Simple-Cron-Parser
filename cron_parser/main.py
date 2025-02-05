import argparse

from cron_parser.cron_parser import SimpleCronParser
from cron_parser.cron_parser_service import CronParserService
from cron_parser.cron_tokenizer import SimpleCronTokenizer
from cron_parser.cron_validator import SimpleCronValidator


def main(cron_string: str) -> None:
    tokenizer = SimpleCronTokenizer()
    validator = SimpleCronValidator()
    parser = SimpleCronParser()
    cron_parser = CronParserService(cron_string, tokenizer, validator, parser)
    result =  cron_parser.parse()
    print(cron_parser.format_output(result))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cron Expression Parser.')
    parser.add_argument('cron_string', type=str, help='Cron string to parse')
    args = parser.parse_args()
    main(args.cron_string)