from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .models import Group, Kid
from .forms import GroupForm, KidForm


def kids_in_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    kids = group.kids.all()  # related_name orqali
    return render(request, 'kids_in_group.html', {'group': group, 'kids': kids})


def group_list_view(request):
    groups = Group.objects.all()
    return render(request, 'group-list.html', {'groups': groups})


def add_group_view(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group-list')
    else:
        form = GroupForm()
    return render(request, 'add_group.html', {'form': form})


def kids_list(request):
    kids = Kid.objects.all()
    ctx = {
        'kids': kids
    }
    return render(request, 'kids.html', ctx)


def kid_add(request):
    form = KidForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('kids-list')
    ctx = {'form': form}
    return render(request, 'kids_add.html', ctx)


def edit_kid(request, pk):
    kid = get_object_or_404(Kid, pk=pk)
    if request.method == 'POST':
        form = KidForm(request.POST, instance=kid)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bola maʼlumotlari yangilandi.')
            return redirect('kids-list')
    else:
        form = KidForm(instance=kid)
    return render(request, 'edit_kid.html', {'form': form, 'kid': kid})


def delete_kid(request, pk):
    kid = get_object_or_404(Kid, pk=pk)
    if request.method == 'POST':
        kid.delete()
        messages.success(request, 'Bola muvaffaqiyatli o‘chirildi.')
        return redirect('kids-list')  # asosiy ro‘yxat sahifangizning URL nomi
    return render(request, 'delete_kid_confirm.html', {'kid': kid})

def kids_view(request):
    # GET parametrdan qidiruv so'zini olish
    search_query = request.GET.get('search', '')

    # Avval barcha bolalarni olish
    kids = Kid.objects.select_related('group').all()

    # Agar qidiruv so'zi mavjud bo'lsa, filterlash
    if search_query:
        kids = kids.filter(full_name__icontains=search_query)

    # Shablon bilan qaytarish
    return render(request, 'kids.html', {
        'kids': kids,
    })
