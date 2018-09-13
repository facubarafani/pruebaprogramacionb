from django import forms
from .models import ToDo
from django.forms import TextInput

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('action_text',)
        widgets = {'action_text': TextInput(attrs={'style': 'width: 100%;', 'placeholder': 'Task'})}