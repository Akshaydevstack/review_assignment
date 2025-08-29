from django.conf import settings

class RegquestMidileware:
    
    def __init__(self,get_response):
        self.get_response=get_response
    
    def __call__(self,request):
        path= request.get_full_path()
        method= request.method

        if getattr(settings, "DEBUG" , False) and not path.startswith(('/static', '/media')):
            print(f"REQ {method} {path}")
        
        response= self.get_response(request)

        return response
