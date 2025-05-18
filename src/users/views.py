from django.contrib.auth.views import LoginView as DjangoLoginView


class LoginView(DjangoLoginView):
    template_name = 'login.html'

class User(DjangoLoginView):
    template_name = 'users.html'
