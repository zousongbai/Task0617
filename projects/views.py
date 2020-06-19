from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index_page(request):
    """定义一个视图"""
    return HttpResponse('<h2>欢迎进入首页</h2>')