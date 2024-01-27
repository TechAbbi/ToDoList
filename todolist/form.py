from .models import TaskToComplete

from django import forms


class TaskToCompleteForm(forms.ModelForm):
    class Meta:
        model = TaskToComplete
        fields = ["task", "completed"]
