from django.contrib import admin
from django.db.models import Count
from django.utils import timezone  # ← ДОБАВИТЬ ЭТОТ ИМПОРТ
from accounts.models import CustomUser
from messages_app.models import Message

class CustomAdminSite(admin.AdminSite):
    site_header = "Администрирование Message App"
    site_title = "Message App Admin"
    index_title = "Панель управления"

admin_site = CustomAdminSite(name='custom_admin')

# Регистрируем модели в кастомной админке
admin_site.register(CustomUser)
admin_site.register(Message)

# Или используем дефолтную админку с кастомным индексом
admin.site.site_header = "Администрирование Message App"
admin.site.site_title = "Message App Admin"
admin.site.index_title = "Панель управления"

# Кастомный индекс для админки
def custom_admin_index(request):
    from django.contrib.admin.views.decorators import staff_member_required
    from django.shortcuts import render
    
    user_stats = CustomUser.objects.aggregate(
        total_users=Count('id'),
        active_users=Count('id', filter=admin.models.Q(is_active=True)),
        staff_users=Count('id', filter=admin.models.Q(is_staff=True)),
    )
    
    message_stats = Message.objects.aggregate(
        total_messages=Count('id'),
        unread_messages=Count('id', filter=admin.models.Q(is_read=False)),
        today_messages=Count('id', filter=admin.models.Q(created_at__date=timezone.now().date())),
    )
    
    recent_messages = Message.objects.select_related('sender', 'recipient').order_by('-created_at')[:10]
    recent_users = CustomUser.objects.order_by('-date_joined')[:10]
    
    context = {
        **admin.site.each_context(request),
        'user_stats': user_stats,
        'message_stats': message_stats,
        'recent_messages': recent_messages,
        'recent_users': recent_users,
    }
    
    return render(request, 'admin/custom_index.html', context)

# Заменяем стандартный индекс админки
admin.site.index = custom_admin_index