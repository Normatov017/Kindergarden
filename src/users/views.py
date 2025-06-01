from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from permissions.permisssion import role_required

from .forms import CustomLoginForm
from .forms import UserForm
from .models import User  # model nomi sizda qanday bo‘lsa, shunga moslang


def login_view(request):
    form = CustomLoginForm()

    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']


            user_obj = authenticate(request, username=username, password=password)
            print(user_obj)
            if user_obj is not None:

                login(request, user_obj)
                messages.success(request, f"Xush kelibsiz, {user_obj.username}!")
                return redirect('home')
            else:
                messages.error(request, "Login yoki parol noto'g'ri.")

    return render(request, 'login.html', {'form': form})

def user_list(request):
    data_user = User.objects.all()
    ctx = {"data_user": data_user}
    return render(request, 'users.html', ctx)










# def user_list(request):
#     data_user = User.objects.select_related('role').all()
#     meals_served = ...
#     return render(request, 'users.html', {
#         'data_user': data_user,
#         'meals_served': meals_served
#     })

def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_edit.html', {'form': form, 'user': user})

def user_delete(request, pk):
    user = get_object_or_404(User, id=pk)

    if request.method == 'POST':
        user.delete()  # Foydalanuvchini o‘chirish
        return redirect('users')  # Foydalanuvchilar ro‘yxatiga qaytish

    return render(request, 'user_confirm_delete.html', {'user': user})
