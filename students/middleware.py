import time

from .models import Logger


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            t1 = time.time()
            response = self.get_response(request)
            t2 = time.time()
            execution_time = t2 - t1
            Logger.objects.create(method=request.method, path=request.path, execution_time=execution_time)
            return response
        else:
            response = self.get_response(request)
            return response
