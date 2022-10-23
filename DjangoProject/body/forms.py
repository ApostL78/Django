from django import forms
from .models import Task
import re
from django.core.exceptions import ValidationError


class TaskForm(forms.ModelForm):
    # title = forms.CharField(label = 'Заголовок' , max_length = 150, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    # task = forms.CharField(label = 'Текст', required = False, widget = forms.Textarea(attrs = {
    #     'class': 'form-control',
    #     'rows': 4,
    # }))
    # is_published = forms.BooleanField(label = 'Состояние', initial = True)
    # category = forms.ModelChoiceField(empty_label = 'Выберите категорию', label = 'Категория', queryset =
    # Categories.objects.all(), widget = forms.Select(attrs ={'class': 'form-control'}))

    class Meta:
        model = Task
        fields = ['title', 'task', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'task': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, }),
            'category': forms.Select(attrs={'class': 'form-control'})
        }
        empty_labels = {
            'category': 'Выберите категорию'
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Цифра в начале')
        return title
