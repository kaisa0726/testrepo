from django.urls import path
from .views import IndexView,PostDetailView,CategoryListView,TagListView,CategoryPostView,TagPostView,SearchPostView,ReplayFormView,CommentFormView
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'blogs'
urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post_detail'),
    path('categories/',CategoryListView.as_view(),name='category_list'),
    path('tags/',TagListView.as_view(),name='tag_list'),
    path('category/<str:category_slug>/',CategoryPostView.as_view(),name='category_post'),
    path('tag/<str:tag_slug>/',TagPostView.as_view(),name='tag_post'),   
    path('search/',SearchPostView.as_view(),name='search_post'),
    path('comment/<int:pk>/',CommentFormView.as_view(),name='comment_form'),
    path('comment/<int:pk>/approve/',views.comment_approve,name='comment_approve'),
    path('commet/<int:pk>/remove/',views.comment_remove,name='comment_remove'),
    path('replay/<int:pk>/',ReplayFormView.as_view(),name='replay_form'),
    path('replay/<int:pk>/approve/',views.replay_approve,name='replay_approve'),
    path('replay/<int:pk>/remove/',views.replay_remove,name='replay_remove'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)