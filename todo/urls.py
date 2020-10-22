from django.urls import path,include
from .views import PostListView

app_name = "todo"

urlpatterns = [
    path('',PostListView.as_view(), name = 'todo-list'),
]
