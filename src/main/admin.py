from django.contrib import admin
from .models import ChatRoom, Message


class MessageInline(admin.TabularInline):
    model = Message
    extra = 0
    readonly_fields = ('timestamp',)
    fields = ('sender', 'content', 'timestamp', 'is_read')
    ordering = ('-timestamp',)


@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'admin', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('user__username', 'admin__username')
    inlines = [MessageInline]

    class Meta:
        verbose_name = 'Chat xonasi'
        verbose_name_plural = 'Chat xonalari'


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat_room', 'sender', 'short_content', 'timestamp', 'is_read')
    list_filter = ('is_read', 'timestamp', 'sender')
    search_fields = ('content', 'sender__username')
    readonly_fields = ('timestamp',)

    def short_content(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content

    short_content.short_description = 'Xabar matni'