#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# 开发时间: 2019/6/30 7:41
# 开发人员: Mikel
# 邮箱地址: plyx_46204@126.com
# 文件名称: views.py
# 开发团队：云飞国际
# 开发工具：PyCharm

from django.http import HttpResponse
from django.shortcuts import render
from . models import Project


def index(request):
    return HttpResponse("Hello world")

def server(request, server_id):
    return HttpResponse("server number is %s" % server_id)

def project(request):
    project_name_list = Project.objects.order_by('id')
    project_name = {'project_name_list': project_name_list}
    return render(request, 'CMDB/project.html', project_name)



