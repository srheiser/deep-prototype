# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Works(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
		verbose_name_plural = "works"

class Edition(models.Model):
    works = models.ForeignKey(Works)
    edition_number = models.CharField(max_length=20)
    changes = models.TextField(null=True, default=None)

    def __str__(self):
		return "%s Edition # %s" % (self.works.title, self.edition_number)

class Copy(models.Model):
    edition = models.ForeignKey(Edition)
    copy_number = models.CharField(max_length=20)
    place = models.CharField(max_length=500)

    def __str__(self):
        return "%s Copy # %s" %(self.edition, self.copy_number)

    class Meta:
		verbose_name_plural = "copies"

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    works = models.ManyToManyField(Works, null=True, blank=True)
    bio = models.TextField(null=True, default=None)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
