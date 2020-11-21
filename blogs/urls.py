from django.urls import path
from .views import IndexView,PostDetailView,TagListView,CategoryListView,TagPostView,CategoryPostView
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'blogs'
urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post_detail'),
    path('categories/',CategoryListView.as_view(),name='category'),
    path('tags/',TagListView.as_view(),name='tags'),
    path('tags/<str:category_slug>/',CategoryListView.as_view(),name='category_post'),
    path('tag/<str:tag_slug>/',TagPostView.as_view(),name='tag_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)