#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# 开发时间: 2019/7/4 6:24
# 开发人员: Mikel
# 邮箱地址: plyx_46204@126.com
# 文件名称: views.py
# 开发团队：云飞国际
# 开发工具：PyCharm

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello world")
    return render(request, 'Devops/index.html')