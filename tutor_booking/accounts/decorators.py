from django.shortcuts import redirect
from functools import wraps

def student_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.role == 'student':
                return view_func(request, *args, **kwargs)
            return redirect('home')
        return redirect('login')
    return _wrapped_view

def tutor_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.role == 'tutor':
                return view_func(request, *args, **kwargs)
            return redirect('home')
        return redirect('login')
    return _wrapped_view

