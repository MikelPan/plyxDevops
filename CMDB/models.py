#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# 开发时间: 2019/6/30 7:52
# 开发人员: Mikel
# 邮箱地址: plyx_46204@126.com
# 文件名称: models.py
# 开发团队：云飞国际
# 开发工具：PyCharm

from django.db import models
from django.contrib.auth.models import User

class Asset(models.Model):
    """所有资产共有数据表"""

    asset_type_choice = (
        ('server', '服务器'),
        ('network_device', '网络设备'),
        ('storage_device', '存储设备'),
        ('security_device', '安全设备'),
        ('software', '软件资产'),
    )

    asset_status = (
        (0, '在线'),
        (1, '下线'),
        (2, '未知'),
        (3, '故障'),
        (4, '备用'),
    )

    asset_type = models.CharField(choices=asset_type_choice, max_length=64, default='server', verbose_name='资产类型')
    name = models.CharField(max_length=64, unique=True, verbose_name='资产名称')
    sn = models.CharField(max_length=128, unique=True, verbose_name='资产序列号')
    business_unit = models.ForeignKey('BusinessUnit', null=True, blank=True, verbose_name='所属业务线',
                                      on_delete=models.SET_NULL)
    status = models.SmallIntegerField(choices=asset_status, default=0, verbose_name='设备状态')
    manufacturer = models.ForeignKey('Manufacturer', null=True, blank=True, verbose_name='制造商',
                                     on_delete=models.SET_NULL)
    manage_ip = models.GenericIPAddressField(null=True, blank=True, verbose_name='管理IP')
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='标签')
    admin = models.ForeignKey(User, null=True, blank=True, verbose_name='资产管理员', related_name='admin',
                              on_delete=models.SET_NULL)
    idc = models.ForeignKey('IDC', null=True, blank=True, verbose_name='所在机房', on_delete=models.SET_NULL)
    contract = models.ForeignKey('Contract', null=True, blank=True, verbose_name='合同', on_delete=models.SET_NULL)
    purchase_day = models.DateField(null=True, blank=True, verbose_name="购买日期")
    expire_day = models.DateField(null=True, blank=True, verbose_name="过保日期")
    price = models.FloatField(null=True, blank=True, verbose_name="价格")
    approved_by = models.ForeignKey(User, null=True, blank=True, verbose_name='批准人', related_name='approved_by',
                                    on_delete=models.SET_NULL)
    memo = models.TextField(null=True, blank=True, verbose_name='备注')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='批准日期')
    m_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')

    def __str__(self):
        return '%s-%s' % (self.get_asset_type_display(), self.name)

    class Meta:
        table_name = 'assent'
        verbose_name = '资产总表'
        verbose_name_plural = "资产总表"
        ordering = ['-c_time']

class Server(models.Model):
    """定义服务器设备"""

    sub_asset_type_choice = (
        (0, 'PC服务器'),
        (1, '刀片机'),
        (2, '小型机'),
        (3, '塔式服务器'),
    )

    created_by_choice = (
        ('auto', '自动添加'),
        ('manual', '手工录入'),
    )


