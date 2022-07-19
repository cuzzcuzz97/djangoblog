from django.shortcuts import render
from .models import Blog
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import redirect, render
import json
# import requests
import time

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
    def image(request):
        img = Photo.objects.all()
        return render_to_response("blog.html", {"img": img})

# def get_currency(request):
    
#     # defining key/request url
#     key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    
#     # requesting data from url

#     data = requests.get(key)  
#     data = data.json()

#     def print_price():
#         return data['price']
       
#     context = {'bitcoin' : print_price}
#     time.sleep(10)
#     return render(request , 'base/main.html', context)