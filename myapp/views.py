from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from myapp.models import Post
from .forms import PostForm



class Index(TemplateView):
    template_name = 'myapp/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'お願いいたします'
        return ctx



class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'myapp/form.html'
    success_url = 'myapp/index.html'