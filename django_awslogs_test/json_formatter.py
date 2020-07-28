import logging
from django.utils import timezone
from json_log_formatter import JSONFormatter
import ujson


class CustomisedJSONFormatter(JSONFormatter):
    json_lib = ujson
    fields = ('levelname', 'name', 'module', 'process', 'thread')

    def json_record(self, message: str, extra: dict, record: logging.LogRecord) -> dict:
        extra['message'] = message
        extra = {field: getattr(record, field) for field in self.fields}

        if 'asctime' not in extra:
            extra['asctime'] = timezone.now()

        if record.exc_info:
            extra['exc_info'] = self.formatException(record.exc_info)

        return extra
