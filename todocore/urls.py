from django.urls import path

from todocore.views import TaskListView, TaskUpdateView

urlpatterns = [
    path("tasks",TaskListView.as_view()),
    path("tasks/<id>",TaskUpdateView.as_view())
]