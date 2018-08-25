# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    comment = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(Blog, related_name="comments")


class Admin(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    upload_at = models.DateTimeField(auto_now=True)
    blogs = models.ManyToManyField(Blog, related_name="admins")
