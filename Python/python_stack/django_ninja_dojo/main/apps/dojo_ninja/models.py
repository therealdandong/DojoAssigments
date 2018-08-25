# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000, default="something string")

    def __repr__(self):
        return "<object {} {} {}>".format(self.name, self.city, self.state)


class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="ninjas")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __repr__(self):
        return "<object {} {}>".format(self.first_name, self.last_name)

"""
the new models add on below.

"""


class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<object: {} {} >".format(self.name, self.desc)


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    Created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    books = models.ManyToManyField(Book, related_name="authors")
    notes = models.TextField(default="some string")

    def __repr__(self):
        return "<object: {} {} {} {}>".format(self.first_name, self.last_name, self.email, self.notes)