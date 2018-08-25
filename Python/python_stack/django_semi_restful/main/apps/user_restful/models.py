# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re


class UserManager(models.Manager):

    def basic_validator(self, postdata):
        email_regex = re.compile(r"^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")
        errors = []
        if len(postdata["first_name"]) < 1:
            errors.append("your first name should not be blank")
        if len(postdata["last_name"]) < 1:
            errors.append("your last name should not be blank")
        if not email_regex.match(postdata["email"]):
            errors.append("you enter a invalid email")

        if errors:
            return (False, errors)
        else:
            user = User.objects.create(first_name=postdata["first_name"], last_name=postdata["last_name"],
                                       email=postdata["email"])
            return (True, user)

    def basic_updater (self,postdata, id):
        email_regex = re.compile(r"^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")
        errors = []
        if len(postdata["first_name"]) < 1:
            errors.append("your first name should not be blank")
        if len(postdata["last_name"]) < 1:
            errors.append("your last name should not be blank")
        if not email_regex.match(postdata["email"]):
            errors.append("you enter a invalid email")
        if errors:
            return (False, errors)
        else:
            user = User.objects.get(id=id)
            user.first_name = postdata["first_name"]
            user.last_name = postdata["last_name"]
            user.email = postdata["email"]
            user.save()
            return (True, user)


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return "<object {} {} {} {}>".format(self.first_name, self.last_name, self.email, self.created_at)