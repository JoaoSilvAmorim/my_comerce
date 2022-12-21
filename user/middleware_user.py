import json
from django.http import HttpResponseForbidden

class middleware_user:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        print('call', request.user)
        return response

    def process_view(self, request, func, args, kwargs):
        try:
            print(request.user)
            print('asd ', list(request.user.get_all_permissions()))
            if request.body:
                data = json.loads(request.body.decode())
            else:
                data = {}
            if not "role" in data:
                return None
            if data["role"] in {}:
                return None
            return HttpResponseForbidden("Seu usuario não tem permissão para acessar essa view")
        except:
            return None