#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# 开发时间: 2019/6/30 7:52
# 开发人员: Mikel
# 邮箱地址: plyx_46204@126.com
# 文件名称: models.py
# 开发团队：云飞国际
# 开发工具：PyCharm

from django.db import models

class Server_Group(models.Model):
    '''主机表'''
    # 创建唯一约束
    name = models.CharField(u'主机组', max_length=100, unique=True)
    # 关联的项目字段
    project = models.ForeignKey('Project', verbose_name='项目名称', on_delete=models.CASCADE)
    # 备注字段
    memo = models.CharField(u'备注', max_length=100, blank=True)
    # 返回值
    def __str__(self):
        return '%s-%s' % (self.name, self.project)

    # 定义Meta属性
    class Meta:
        db_table = 'server_group'
        unique_together = (('name', 'project'),)
        indexes = [
            models.Index(fields=['name', 'project']),
            models.Index(fields=['name'], name='name_idx'),
        ]

class Project(models.Model):
    '''项目表'''
    # 创建唯一约束
    name = models.CharField(u'项目名称', max_length=100, unique=True)
    # 备注字段
    memo = models.CharField(u'备注', max_length=100, blank=True)
    # 返回值
    def __str__(self):
        return self.name

    # 定义Meta属性
    class Meta:
        db_table = 'project'

