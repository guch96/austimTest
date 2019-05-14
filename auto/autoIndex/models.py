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
    status_choices = (
        (0, '未通过'),
        (1, '已通过'),
        (2, '申请中')
    )
    iTask=models.ForeignKey('testTask',on_delete=models.CASCADE)
    iName=models.CharField(max_length=100)
    iurl=models.CharField(max_length=100)
    iHttp=models.CharField(max_length=10)
    iType=models.CharField(max_length=10)
    iStatus=models.IntegerField(choices=status_choices,default=2)
    def __str__(self):
        return self.iName.encode('utf-8')

class apiHeader(models.Model):
    apiId=models.ForeignKey('testInterface',on_delete=models.CASCADE)
    key=models.CharField(max_length=100,null=True)
    key_description = models.CharField(max_length=100, null=True, blank=True)
    key_value = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return str(self.apiId)

boby_types=(
    ('raw','raw'),
    ('form-data','form-data'),
    ('x-www-form-urlencoded','x-www-form-urlencoded')
)

class apiBody(models.Model):
    apiId=models.ForeignKey('testInterface',on_delete=models.CASCADE)
    body_type=models.CharField(max_length=100,choices=boby_types)
    body_content=models.CharField(max_length=100,null=True,blank=True)
    body_key=models.CharField(max_length=100,null=True)
    body_values=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return str(self.apiId)
class apiParams(models.Model):
    apiId = models.ForeignKey('testInterface', on_delete=models.CASCADE)
    key = models.CharField(max_length=100, null=True)
    key_description = models.CharField(max_length=100, null=True, blank=True)
    key_value = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return str(self.apiId)
