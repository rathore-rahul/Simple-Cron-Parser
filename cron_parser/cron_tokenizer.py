from abc import ABC, abstractmethod


class CronTokenizer(ABC):
    @abstractmethod
    def tokenize(self, cron_expression):
        pass


class SimpleCronTokenizer(CronTokenizer):
    def tokenize(self, cron_expression):
        tokens = cron_expression.split(' ')
        cron_tokens = []
        for i, token in enumerate(tokens):
            if not token.startswith('/'):
                # this is one of the time pattern
                cron_tokens.append(token)
            else:
                # this is command so no more token parsing after this
                command = ' '.join(tokens[i:])
                cron_tokens.append(command)
                break
        return cron_tokens






