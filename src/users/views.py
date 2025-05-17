from django.contrib.auth.views import LoginView as DjangoLoginView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class LoginView(DjangoLoginView):
    template_name = 'login.html'


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')