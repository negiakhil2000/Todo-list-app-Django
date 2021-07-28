from django import views
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from taskLister.views import TasksListView, TasksCreate
from taskLister.views import delete_task

app_name='taskLister'

urlpatterns=[
    path('',TasksListView.as_view(),name='tasks-list'),
    path('form/',TasksCreate.as_view(),name='tasks-form'), 
    url(r'^delete/(?P<task_id>[0-9]+)/$',delete_task, name='delete-task'),
] 
