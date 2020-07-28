import logging
from django.utils import timezone
from json_log_formatter import JSONFormatter
import ujson


class CustomisedJSONFormatter(JSONFormatter):
    json_lib = ujson

    def json_record(self, message: str, extra: dict, record: logging.LogRecord) -> dict:
        extra['message'] = message

        # Include builtins
        extra['level'] = record.levelname
        extra['name'] = record.name

        if 'time' not in extra:
            extra['time'] = timezone.now()

        if record.exc_info:
            extra['exc_info'] = self.formatException(record.exc_info)

        return extra
