from django.urls import path,include
from .views import PostListView
from .views import todo

app_name = "todo"

urlpatterns = [
    path('',PostListView.as_view(), name = 'todo-list'),
    path('a', todo, name = "index"),
]
