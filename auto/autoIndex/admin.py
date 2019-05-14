# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import testProject,testTask,testInterface,apiBody,apiHeader,apiParams
# Register your models here.
admin.site.register(testProject)
admin.site.register(testTask)
admin.site.register(testInterface)
admin.site.register(apiHeader)
admin.site.register(apiBody)
admin.site.register(apiParams)