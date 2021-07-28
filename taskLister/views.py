
from django.conf.urls import url
from django.http import response
from django.http.response import ResponseHeaders
from taskLister.templates.taskLister.forms import TasksForm
from django.db import models
from taskLister.models import Tasks
# from django.views.generic.list import ListView
from taskLister.models import Tasks
from django.views.generic import ListView, CreateView
from django.urls import reverse
from django.http import request
from django.shortcuts import redirect, render


class TasksCreate(CreateView):
    
    template_name='taskLister/tasks_create_form.html'
    
    model = Tasks
    fields = ['task_title']
    def get_success_url(self):
        return reverse('taskLister:tasks-list', kwargs={})

    

class TasksListView(ListView):
    model=Tasks
    context_object_name='tasks_list'




def delete_task(request,task_id=None):
    task=Tasks.objects.filter(pk=task_id)
    task.delete()
    return redirect('taskLister:tasks-list')
    