from django.db.models import Count,Q
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Post,Category,Tag
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,redirect
from django.views.generic.edit import CreateView
from .forms import CommentForm,ReplayForm
from .models import Post,Category,Tag,Comment,Replay
class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.is_public and not self.request.user.is_authenticated:
            raise Http404
        return obj
        
class CategoryListView(ListView):
    queryset = Category.objects.annotate(
        num_posts=Count('post',filter=Q(post__is_public=True)))
        

class TagListView(ListView):
    queryset = Tag.objects.annotate(
        num_posts = Count('post',filter=Q(post__is_public=True)))

class IndexView(ListView):
    model = Post
    template_name = 'blogs/index.html'
    paginate_by = 2
    contex_object_name = 'index'


class CategoryPostView(ListView):
    model = Post
    template_name = 'blogs/category_post.html'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        self.category = get_object_or_404(Category,slug=category_slug)
        qs = super().get_queryset().filter(category=self.category)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        return context
    
class TagPostView(ListView):
    model = Post
    template_name = 'blogs/tag_post.html'

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        self.tag = get_object_or_404(Tag,slug=tag_slug)
        qs = super().get_queryset().filter(Tag,slug=tag_slug)
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.tag
        return context
    