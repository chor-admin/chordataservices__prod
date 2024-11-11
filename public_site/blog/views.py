from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView



from .models import BlogStartPost, BlogRunPost, BlogExitPost

class BlogStartView(ListView):
    template_name = 'blog/blog_start.html'
    queryset = BlogStartPost.objects.all()
    paginate_by = 2

class PostStartView(DetailView):
    model = BlogStartPost
    template_name = 'blog/blog_start_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # since our slug field is not unique, we need the primary key to get a unique post
        pk = self.kwargs['pk']
        slug = self.kwargs['slug']

        post = get_object_or_404(BlogStartPost, pk=pk, slug=slug)
        context['post'] = post
        return context


class BlogRunView(ListView):
    template_name = 'blog/blog_run.html'
    queryset = BlogRunPost.objects.all()
    paginate_by = 2

class PostRunView(DetailView):
    model = BlogRunPost
    template_name = 'blog/blog_run_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # since our slug field is not unique, we need the primary key to get a unique post
        pk = self.kwargs['pk']
        slug = self.kwargs['slug']

        post = get_object_or_404(BlogRunPost, pk=pk, slug=slug)
        context['post'] = post
        return context


class BlogExitView(ListView):
    template_name = 'blog/blog_exit.html'
    queryset = BlogExitPost.objects.all()
    paginate_by = 10

class PostExitView(DetailView):
    model = BlogExitPost
    template_name = 'blog/blog_exit_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # since our slug field is not unique, we need the primary key to get a unique post
        pk = self.kwargs['pk']
        slug = self.kwargs['slug']

        post = get_object_or_404(BlogExitPost, pk=pk, slug=slug)
        context['post'] = post
        return context

