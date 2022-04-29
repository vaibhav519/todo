from django import forms
from . models import TodoContent


class ToDoForm(forms.ModelForm):
    class Meta:
        model = TodoContent
        fields = ['todo_text']

        widgets = {
            'todo_text': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': "Enter Task"})
        }
