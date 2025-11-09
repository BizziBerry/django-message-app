from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from .forms import MessageForm
from .models import Message

def home_view(request):
    return render(request, 'messages_app/home.html')

@login_required
def send_message_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': 'Сообщение успешно отправлено!'
                })
            else:
                messages.success(request, 'Сообщение успешно отправлено!')
                return redirect('send_message')
    else:
        form = MessageForm()
    
    return render(request, 'messages_app/send_message.html', {'form': form})
    
   