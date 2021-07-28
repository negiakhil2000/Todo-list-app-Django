from django import forms
from django.db.models import fields
from taskLister.models import Tasks

class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields=['task_title']
        