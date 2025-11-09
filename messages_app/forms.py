'''from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'message_text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message_text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Введите ваше сообщение (максимум 500 символов)'
            }),
        }
    
    def clean_message_text(self):
        message_text = self.cleaned_data.get('message_text')
        if not message_text:
            raise forms.ValidationError("Сообщение не может быть пустым.")
        if len(message_text) > 500:
            raise forms.ValidationError("Сообщение не должно превышать 500 символов.")
        return message_text'''
        
        
from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'message_text']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
            }),
            'message_text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Введите ваше сообщение (максимум 500 символов)'
            }),
        }
        labels = {
            'name': 'Имя',                    # МЕНЯЕМ НА РУССКИЙ
            'email': 'Email',  
            'message_text': 'Сообщение',      # МЕНЯЕМ НА РУССКИЙ
        }
    
    def clean_message_text(self):
        message_text = self.cleaned_data.get('message_text')
        if not message_text:
            raise forms.ValidationError("Сообщение не может быть пустым.")
        if len(message_text) > 500:
            raise forms.ValidationError("Сообщение не должно превышать 500 символов.")
        return message_text       
        
