# main/views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, Message
from django.utils import timezone
import random

def home_view(request):
    return render(request, 'index.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')


@login_required
def chat_view(request):
    chat_room, created = ChatRoom.objects.get_or_create(
        user=request.user,
        defaults={'is_active': True}
    )

    if not chat_room.admin and request.user.is_staff:
        chat_room.admin = request.user
        chat_room.save()

    # So'nggi 50 ta xabarni olib kelish
    initial_messages = Message.objects.filter(chat_room=chat_room).order_by('timestamp')[:50]

    # Oxirgi xabar ID sini olish (query slicing'dan oldin!)
    last_message = Message.objects.filter(chat_room=chat_room).order_by('-timestamp').first()

    return render(request, 'chatbox.html', {
        'chat_room': chat_room,
        'initial_messages': initial_messages,
        'last_message_id': last_message.id if last_message else 0,
    })


@login_required
def send_message(request):
    if request.method == 'POST':
        chat_room = get_object_or_404(ChatRoom, user=request.user)
        content = request.POST.get('content', '').strip()

        if content:
            # Yangi xabarni yaratish
            message = Message.objects.create(
                chat_room=chat_room,
                sender=request.user,
                content=content
            )

            return JsonResponse({
                'status': 'success',
                'message_id': message.id,
                'timestamp': message.timestamp.strftime('%H:%M %p')
            })

    return JsonResponse({'status': 'error'}, status=400)


@login_required
def get_messages(request):
    chat_room = get_object_or_404(ChatRoom, user=request.user)
    last_message_id = request.GET.get('last_id', 0)

    messages = Message.objects.filter(
        chat_room=chat_room,
        id__gt=last_message_id
    ).order_by('timestamp')

    messages_list = [{
        'id': msg.id,
        'sender': msg.sender.username,
        'content': msg.content,
        'timestamp': msg.timestamp.strftime('%H:%M %p'),
        'is_admin': msg.sender.is_staff
    } for msg in messages]

    return JsonResponse({'messages': messages_list})