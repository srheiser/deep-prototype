# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.template import Context, Template
from django.shortcuts import render, get_object_or_404
from django.template import loader
import models
from .models import *
from django.contrib import admin
from django.urls import reverse

def index(request):
    return HttpResponse("Hello, user! You're at the deep index.")
