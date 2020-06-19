# -*- coding:utf-8 -*-
# @Author       : 小青年
# @ProjectName  :Task0617
# @File         : urls.py
# @Time         : 2020/6/17 10:07

from django.urls import path

# 导入视图
from projects.views import index_page
urlpatterns=[
    path('index/',index_page)
]