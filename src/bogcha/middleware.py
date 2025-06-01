from django.shortcuts import redirect
from django.conf import settings

EXEMPT_URLS = [
    settings.LOGIN_URL,  # asosan '/accounts/login/'
    '/users/login/',     # agar kerak bo‘lsa
    '/admin/login/',     # admin login sahifasi
    '/static/',          # statik fayllar uchun
]

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Agar foydalanuvchi tizimga kirmagan va url istisno ro'yxatida bo'lmasa, login sahifaga yo'naltirilsin
        if not request.user.is_authenticated:
            path = request.path
            if not any(path.startswith(url) for url in EXEMPT_URLS):
                return redirect(settings.LOGIN_URL)
        return self.get_response(request)
