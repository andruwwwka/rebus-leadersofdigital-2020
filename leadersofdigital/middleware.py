from django.utils.deprecation import MiddlewareMixin


class CorsMiddleware(MiddlewareMixin):

    def process_response(self, req, resp):
        resp['Access-Control-Allow-Origin'] = '*'
        resp['Access-Control-Allow-Headers'] = '*'
        return resp
