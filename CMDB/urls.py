#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# 开发时间: 2019/6/30 7:44
# 开发人员: Mikel
# 邮箱地址: plyx_46204@126.com
# 文件名称: urls.py
# 开发团队：云飞国际
# 开发工具：PyCharm

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:server_id>/', views.server, name='server'),
    path('project/', views.project, name='project'),

]
