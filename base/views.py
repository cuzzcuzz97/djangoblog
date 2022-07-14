from django.shortcuts import render
from .models import Blog
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import redirect, render

class BlogList(ListView):
    model = Blog
    context_object_name = 'blogs'
    def image(request):
        img = Photo.objects.all()
        return render_to_response("blog_list.html", {"img": img})

class BlogDetail(DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'base/blog.html'
