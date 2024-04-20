from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_fanction):
    def wraper_function(request, *args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_fanction
        
def allowed_users(allowed_roles=[]):
    def decorator(view_function):
        def wraper_function(request, *args,**kwargs):
            return view_function(request, *args,**kwargs)
        return wraper_function
    return decorator