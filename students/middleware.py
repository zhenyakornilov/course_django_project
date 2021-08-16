import time
import datetime

from .views import create_student

from .models import Logger


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            print('GOOD')
            t1 = time.time()
            print(request.path)
            response = self.get_response(request)
            t2 = time.time()
            execution_time = t2-t1
            print(execution_time)
            Logger.objects.create(method=request.method, path=request.path, execution_time=execution_time)
            return response
        else:
            response = self.get_response(request)
            return response




