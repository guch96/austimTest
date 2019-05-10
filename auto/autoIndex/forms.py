# -*- coding: utf-8 -*-
from django import forms
class formTask(forms.Form):
    name=forms.CharField(max_length=100,required=True)
    host=forms.CharField(max_length=100,required=True,strip=True)
    # po=forms.CharField(max_length=100,required=True,strip=True)
    port=forms.IntegerField()
class formProject(forms.Form):
    name=forms.CharField(max_length=100,required=True)

class formInterface(forms.Form):
    iName = forms.CharField(max_length=100,required=True)
    iurl = forms.CharField(max_length=100,required=True)
    iHttp = forms.CharField(max_length=10,required=True)
    iType = forms.CharField(max_length=10,required=True)