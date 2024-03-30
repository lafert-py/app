import re
from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


def index(request):
    context = {
        "title": "Home page",
        "content": "Welcome to the home page of the app",
        "list": ["item1", "item2", "item3"],
        "dict": {"key1": "value1", "key2": "value2"},
        "is_authenticated": True,
    }
    return render(request, "main/index.html", context)


def about(request):
    return HttpResponse("About page of the app")
