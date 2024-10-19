import time
from django.utils.deprecation import MiddlewareMixin

class QueryTimingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Store the start time when the request is received
        request.start_time = time.time()cd
    def process_response(self, request, response):
        # Calculate the total time taken for the request
        if hasattr(request, 'start_time'):
            total_time = time.time() - request.start_time
            # Log the time taken (you can replace this with actual logging)
            print(f"Time taken for {request.path}: {total_time:.4f} seconds")

        return response
