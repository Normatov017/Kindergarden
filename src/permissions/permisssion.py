from functools import wraps
from django.http import JsonResponse
from django.shortcuts import render

def role_required(*role_names):
    normalized_roles = [r.lower() for r in role_names]
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user = request.user
            if user.is_authenticated:
                user_role = getattr(user.role, 'name', '').lower()
                if user_role in normalized_roles:
                    return view_func(request, *args, **kwargs)
                return render(request, '404.html')
            return render(request, '404.html')
        return _wrapped_view
    return decorator
