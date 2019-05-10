# -*- coding: utf-8 -*-
# Create your models here.
from __future__ import unicode_literals

from django.db import models

class testProject(models.Model):
    tName=models.CharField(max_length=100)
    def __str__(self):
        return self.tName.encode('utf-8')

class testTask(models.Model):
    pName=models.CharField(max_length=100)
    pHost=models.CharField(max_length=100)
    pPort=models.IntegerField()
    pProject=models.ForeignKey('testProject',on_delete=models.CASCADE)
    def __str__(self):
        return  self.pName.encode('utf-8')
    # class Meta:
    #     unique_together = ('', '',)

class testInterface(models.Model):
    status_choices = {
        (0, '未通过'),
        (1, '已通过'),
        (2, '申请中')
    }
    iTask=models.ForeignKey('testTask',on_delete=models.CASCADE)
    iName=models.CharField(max_length=100)
    iurl=models.CharField(max_length=100)
    iHttp=models.CharField(max_length=10)
    iType=models.CharField(max_length=10)
    iStatus=models.IntegerField(choices=status_choices,default=2)
