from django.contrib import messages

from .models import Kid
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import KidForm
from .forms import KidCreateUpdateForm

def kids_list(request):
    kids = Kid.objects.select_related('group').all()
    return render(request, 'kids.html', {'kids': kids})








# Faqat superuser yoki staff foydalanuvchilar kirishi mumkin
def is_admin(user):
    return user.is_staff or user.is_superuser

@login_required
@user_passes_test(is_admin)
def add_kid(request):
    if request.method == 'POST':
        form = KidForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kid-list')  # o'zingizga mos URL nomi
    else:
        form = KidForm()

    return render(request, 'kids_add.html', {'form': form})








def edit_kid(request, pk):
    kid = get_object_or_404(Kid, pk=pk)
    if request.method == 'POST':
        form = KidCreateUpdateForm(request.POST, instance=kid)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bola maʼlumotlari yangilandi.')
            return redirect('kids-list')
    else:
        form = KidCreateUpdateForm(instance=kid)
    return render(request, 'edit_kid.html', {'form': form, 'kid': kid})




def delete_kid(request, pk):
    kid = get_object_or_404(Kid, pk=pk)
    if request.method == 'POST':
        kid.delete()
        messages.success(request, 'Bola muvaffaqiyatli o‘chirildi.')
        return redirect('kids-list')  # asosiy ro‘yxat sahifangizning URL nomi
    return render(request, 'delete_kid_confirm.html', {'kid': kid})