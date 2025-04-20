from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        required=False
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'deadline']
