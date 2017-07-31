# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Works)
admin.site.register(Edition)
admin.site.register(Copy)
admin.site.register(Author)
