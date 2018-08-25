# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["name"])< 5:
            errors["name"] = "Blog name should be more than 5 character."
        if len(postData["desc"])< 15:
            errors["desc"] = "Blog description should be more than 15 character"
        return errors










class Blog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager



