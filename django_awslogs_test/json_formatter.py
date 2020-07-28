import logging
from django.utils import timezone
from json_log_formatter import JSONFormatter
import ujson


class CustomisedJSONFormatter(JSONFormatter):
    json_lib = ujson
    fields = ('levelname', 'name', 'module', 'processName', 'threadName', 'pathname')
    unjsonable = ('request',)

    def json_record(self, message: str, extra: dict, record: logging.LogRecord) -> dict:
        extra['message'] = message

        for field in self.fields:
            extra[field] = getattr(record, field)

        for field in self.unjsonable:
            extra.pop(field, None)

        if 'asctime' not in extra:
            extra['asctime'] = timezone.now()

        if record.exc_info:
            extra['exc_info'] = self.formatException(record.exc_info)

        return extra
