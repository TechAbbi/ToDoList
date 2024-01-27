from .models import TaskToComplete

from django import forms


# class TaskToCompleteForm(forms.ModelForm):
#     class Meta:
#         model = TaskToComplete
#         fields = ["task", "completed"]

class TaskToCompleteForm(forms.Form):
    task = forms.CharField(max_length=45, widget=forms.TextInput(
        attrs={
            "class ": "form-control",
            "placeholder": "Enter todo e.g. Wash my car",
            "aria-label": "Todo",
            "aria-describedby": "add-btn",
        }
    ))
