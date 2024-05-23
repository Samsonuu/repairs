from django.shortcuts import redirect, render

def login_required_message(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'please_login.html')
        return view_func(request, *args, **kwargs)
    return _wrapped_view
    