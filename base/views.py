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

# def mmdv(request):
#     coindisplay = Coinlist.objects.all()
#     return render(request, "blog_list.html", {"Coinlist": coindisplay})

# class Coinlist(ListView):
#     model = Coinlist
#     context_object_name = 'coins'



    # def get_currency(request):

    #     key = "https://api.binance.com/api/v3/ticker/24hr"

    #     def print_price(coinname):
    #         data = requests.get(key)
    #         data = data.json()
    #         price = next(z for z in data if z["symbol"] == f"{coinname}")
    #         coin_price = price.get("lastPrice")
    #         return coin_price
    #     token_price = print_price("BTCUSDT")

    #     context = {'bitcoin' : token_price }

    #     return render(request , 'blog_list.html', context)