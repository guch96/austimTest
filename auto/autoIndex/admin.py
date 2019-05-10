# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import testProject,testTask
# Register your models here.
admin.site.register(testProject)
admin.site.register(testTask)