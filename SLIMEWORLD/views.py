from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "genre.html", {})


class HomeView(TemplateView):
    template_name = 'genre.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        num = None
        some_list = [
            random.randint(0, 100000000),
            random.randint(0, 100000000),
            random.randint(0, 100000000)
        ]
        condition_bool_item = True
        if condition_bool_item:
            num = random.randint(0, 100000000)
        context = {
            "num": num,
            "some_list": some_list
        }
        return context
