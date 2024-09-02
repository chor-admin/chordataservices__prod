from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView


from .models import BlogStartPost

class BlogStartView(ListView):
    template_name = 'blog/blog_start.html'
    queryset = BlogStartPost.objects.all()
    paginate_by = 2

class PostView(DetailView):
    model = BlogStartPost
    template_name = 'blog/blog_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # since our slug field is not unique, we need the primary key to get a unique post
        pk = self.kwargs['pk']
        slug = self.kwargs['slug']

        post = get_object_or_404(BlogStartPost, pk=pk, slug=slug)
        context['post'] = post
        return context




