from .models import Post
from django.views.generic import ListView

class PostListView(ListView):   
    model = Post
    template_name = 'todo/base.htm'
    ordering = ['-datetime']

    def get_queryset(self):
        queryset = Post.objects.all()
        if 'query' in self.request.GET:
            qs = self.request.GET['query']
            queryset = queryset.filter(name__contains = qs)
        return queryset







