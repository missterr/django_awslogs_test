from django.http import HttpResponse
import logging

common = logging.getLogger(__name__)
informator = logging.getLogger('informator')


def test_logging(request):
    common.error('Common logger error.')
    informator.debug('Informators test log message.')

    return HttpResponse('Everything is ok')


def test_exception(request):
    raise ZeroDivisionError
    return HttpResponse('Everything is ok')
