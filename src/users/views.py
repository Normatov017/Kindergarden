# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomLoginForm
from .models import User  # bu sizning custom user model
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.http import HttpResponse

from django.contrib import messages

def login_view(request):
    form = CustomLoginForm()

    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Django'ning autentifikatsiya qilish funksiyasidan foydalanamiz
            user_obj = authenticate(request, username=username, password=password)
            print(user_obj)
            if user_obj is not None:
                # Foydalanuvchini tizimga kiritamiz
                login(request, user_obj)
                messages.success(request, f"Xush kelibsiz, {user_obj.username}!")
                return redirect('home')  # Dashboard URL nomi
            else:
                messages.error(request, "Login yoki parol noto'g'ri.")

    return render(request, 'login.html', {'form': form})
def user_list(request):
    if request.user.is_authenticated and request.user.role is not None:
        if request.user.role.name in ["superuser", "manager"]:
            data_user = User.objects.all()
            ctx = {"data_user": data_user}
            return render(request, 'users.html', ctx)
    return HttpResponse("Sizga ruxsat berilmagan", status=403)
