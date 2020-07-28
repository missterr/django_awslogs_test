from logging import LogRecord, Filter

import ujson
from django.utils import timezone
from django.conf import settings
from json_log_formatter import JSONFormatter


class CustomisedJSONFormatter(JSONFormatter):
    """Custom JSON formatter"""
    json_lib = ujson
    fields = ('levelname', 'name', 'module', 'processName', 'threadName', 'pathname')
    unjsonable = ('request', )

    def json_record(self, message: str, extra: dict, record: LogRecord) -> dict:
        extra['message'] = message

        for field in self.fields:
            extra[field] = getattr(record, field)

        for field in self.unjsonable:
            extra.pop(field, None)

        extra['server_time'] = timezone.now().strftime('%Y-%m-%d %H:%M:%S.%f')

        if record.exc_info:
            extra['exc_info'] = self.formatException(record.exc_info)

        return extra


class CustomFilter(Filter):
    """Logging filter that adds app_name field to each log record"""
    def filter(self, record: LogRecord) -> int:
        record.app_name = settings.APP_NAME
        return True
