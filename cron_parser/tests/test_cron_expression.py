import unittest
from cron_parser.cron_parser import SimpleCronParser
from cron_parser.cron_parser_service import CronParserService
from cron_parser.cron_tokenizer import SimpleCronTokenizer
from cron_parser.cron_validator import SimpleCronValidator


class TestCronParser(unittest.TestCase):
    def setUp(self):
        self.tokenizer = SimpleCronTokenizer()
        self.validator = SimpleCronValidator()
        self.parser = SimpleCronParser()

    def parse_cron(self, cron_string):
        return CronParserService(cron_string, self.tokenizer, self.validator, self.parser).parse()

    def test_default_cron_string(self):
        cron_string = "*/15 6 1,15 * 1-5 /usr/bin/find"
        value = self.parse_cron(cron_string)

        self.assertEqual(value.get('minute'), [0, 15, 30, 45])
        self.assertEqual(value.get('hour'), [6])
        self.assertEqual(value.get('day of month'), [1,15])
        self.assertEqual(value.get('month'), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        self.assertEqual(value.get('day of week'), [1, 2, 3, 4, 5])
        self.assertEqual(value.get('command'), '/usr/bin/find')

    def test_wildcard(self):
        cron_string = "* * * * * /usr/bin/find"
        value = self.parse_cron(cron_string)

        self.assertEqual(value.get('minute'), list(range(0, 60)))
        self.assertEqual(value.get('hour'), list(range(0, 24)))
        self.assertEqual(value.get('day of month'), list(range(1, 32)))
        self.assertEqual(value.get('month'), list(range(1, 13)))
        self.assertEqual(value.get('day of week'), list(range(1, 8)))
        self.assertEqual(value.get('command'), '/usr/bin/find')

    def test_comma(self):
        cron_string = "1,2,3,4 7,8,9 25,26 1,2 6,7 /usr/bin/find"
        value = self.parse_cron(cron_string)

        self.assertEqual(value.get('minute'), [1, 2, 3, 4])
        self.assertEqual(value.get('hour'), [7, 8, 9])
        self.assertEqual(value.get('day of month'), [25, 26])
        self.assertEqual(value.get('month'), [1, 2])
        self.assertEqual(value.get('day of week'), [6, 7])
        self.assertEqual(value.get('command'), '/usr/bin/find')

    def test_range(self):
        cron_string = "1-5 6-10 15-20 1-12 1-7 /usr/bin/find"
        value = self.parse_cron(cron_string)

        self.assertEqual(value.get('minute'), list(range(1, 6)))
        self.assertEqual(value.get('hour'),  list(range(6, 11)))
        self.assertEqual(value.get('day of month'), list(range(15, 21)))
        self.assertEqual(value.get('month'), list(range(1, 13)))
        self.assertEqual(value.get('day of week'), list(range(1, 8)))
        self.assertEqual(value.get('command'), '/usr/bin/find')

    def test_step_range(self):
        cron_string = "*/5 */2 */3 */4 */2 /usr/bin/find"
        value = self.parse_cron(cron_string)

        self.assertEqual(value.get('minute'), list(range(0, 60, 5)))
        self.assertEqual(value.get('hour'), list(range(0, 24, 2)))
        self.assertEqual(value.get('day of month'),  list(range(1, 32, 3)))
        self.assertEqual(value.get('month'), list(range(1, 13, 4)))
        self.assertEqual(value.get('day of week'), list(range(1, 8, 2)))
        self.assertEqual(value.get('command'), '/usr/bin/find')

    def test_step_range_with_with_beginning(self):
        cron_string = "2/5 5/2 10/3 5/4 3/2 /usr/bin/find"
        value = self.parse_cron(cron_string)

        self.assertEqual(value.get('minute'), list(range(2, 60, 5)))
        self.assertEqual(value.get('hour'), list(range(5, 24, 2)))
        self.assertEqual(value.get('day of month'), list(range(10, 32, 3)))
        self.assertEqual(value.get('month'), list(range(5, 13, 4)))
        self.assertEqual(value.get('day of week'), list(range(3, 8, 2)))
        self.assertEqual(value.get('command'), '/usr/bin/find')

    def test_value(self):
        cron_string = "1 6 15 11 5 /usr/bin/find"
        value = self.parse_cron(cron_string)

        self.assertEqual(value.get('minute'), [1])
        self.assertEqual(value.get('hour'), [6])
        self.assertEqual(value.get('day of month'), [15])
        self.assertEqual(value.get('month'), [11])
        self.assertEqual(value.get('day of week'), [5])
        self.assertEqual(value.get('command'), '/usr/bin/find')

    def test_command_with_args(self):
        cron_string = "1 6 15 11 5 /usr/bin/find -v 1 2 3"
        value = self.parse_cron(cron_string)

        self.assertEqual(value.get('minute'), [1])
        self.assertEqual(value.get('hour'), [6])
        self.assertEqual(value.get('day of month'), [15])
        self.assertEqual(value.get('month'), [11])
        self.assertEqual(value.get('day of week'), [5])
        self.assertEqual(value.get('command'), '/usr/bin/find -v 1 2 3')

    def test_year_extension(self):
        cron_string = "1 6 15 11 5 2025-2030 /usr/bin/find -v 1 2 3"
        value = self.parse_cron(cron_string)

        self.assertEqual(value.get('minute'), [1])
        self.assertEqual(value.get('hour'), [6])
        self.assertEqual(value.get('day of month'), [15])
        self.assertEqual(value.get('month'), [11])
        self.assertEqual(value.get('day of week'), [5])
        self.assertEqual(value.get('year'), [2025, 2026, 2027, 2028, 2029, 2030])
        self.assertEqual(value.get('command'), '/usr/bin/find -v 1 2 3')
