# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
email_regex = re.compile('^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')
name_regex = re.compile('([a-zA-Z]+)')


class UserManager(models.Manager):

    def basic_validator(self, postdata):
        errors = []
        if len(postdata["first_name"]) < 2 or not name_regex.match(postdata["first_name"]):
            errors.append("first name must be more than 2 character and letter only.")
        if len(postdata["last_name"]) < 2 or not name_regex.match(postdata["last_name"]):
            errors.append("first name must be more than 2 character and letters only.")
        if not email_regex.match(postdata["email"]):
            errors.append("please enter a valid email")
        if postdata["password"] != postdata["password_confirm"]:
            errors.append("password didnt match")
        if errors:
            return (False, errors)
        else:
            hash1 = bcrypt.hashpw(postdata["password"].encode(), bcrypt.gensalt())
            user=User.objects.create(first_name=postdata["first_name"], last_name=postdata["last_name"],
                                     email=postdata["email"], password=hash1)
            return (True, user)

    def login_checker(self,postdata):
        errors = []
        if len(User.objects.filter(email=postdata["email"])) < 1:
            errors.append("please enter a valid password")
        if not bcrypt.checkpw(postdata["password"].encode(), User.objects.get(email=postdata["email"]).password.encode()):
            errors.append("password didn't match")

        if errors:
            return (False, errors)
        else:
            user = User.objects.get(email=postdata["email"])
            return (True, user)


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()
