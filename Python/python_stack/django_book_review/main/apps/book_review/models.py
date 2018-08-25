# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
name_regex = re.compile('^[a-zA-Z\s]*$')
email_regex = re.compile('^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')


class UserManager(models.Manager):
    def basic_validator(self, postdata):
        errors = []
        if len(postdata["name"]) < 2 or not name_regex.match(postdata["name"]):
            errors.append("you name should be longer than 2 character, also no special character allowed")
        if len(postdata["alias"]) < 2 or not name_regex.match(postdata["alias"]):
            errors.append("you alias should be longer than 2 character, also no special character allowed")
        if not email_regex.match(postdata["email"]):
            errors.append("you must enter a valid email")
        if len(User.objects.filter(email=postdata["email"])) > 0:
            errors.append("the email you enter have already exist")
        if postdata["password"] != postdata["confirm_password"]:
            errors.append("password doesn't match")
        if len(postdata["password"]) < 8:
            errors.append("password can not be shorter than 8 character.")
        if errors:
            return (False, errors)
        else:
            hash1 = bcrypt.hashpw(postdata["password"].encode(), bcrypt.gensalt())
            user = User.objects.create(name=postdata["name"], alias=postdata["alias"], email=postdata["email"], password=hash1)
            user.save()
            return (True,"you have successful register")

    def login_check(self, postdata):
        errors = []
        if len(User.objects.filter(email=postdata["email"])) < 1:
            errors.append("the email you enter is not valid.")
        if not bcrypt.checkpw(postdata["password"].encode(), User.objects.get(email=postdata["email"]).password.encode()):
            errors.append("the password didn't match")
        if errors:
            return (False, errors)
        else:
            user = User.objects.get(email=postdata["email"])
            return (True, user)


class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()


class AuthorManager(models.Manager):
    def valida_author(self, postdata):
        errors = []
        if postdata["author_drop"] == "NA":
            if name_regex.match(postdata["author_add"]):
                return (True, postdata["author_add"])
            else:
                errors.append("the author you add is invalid")
                return (False, errors)
        else:
            author = postdata["author_drop"]
            return (True, author)


class Author(models.Model):
    name = models.CharField(max_length=255)
    objects = AuthorManager()


class BookManager(models.Manager):
    def valida_book(self, postdata):
        errors = []
        if len(postdata["book_title"]) < 1 or not name_regex.match(postdata["book_title"]):
            errors.append("book title is invalid")
            return (False, errors)
        else:
            return (True, postdata["book_title"])


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books")
    Created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()


class ReviewManager(models.Manager):
    def valida_review(self, postdata):
        errors = []
        if len(postdata["review"]) < 1:
            errors.append("review can't be empty")
            return (False, errors)
        else:
            return (True, (postdata["review"], postdata["rating"]))


class Review(models.Model):
    star = models.IntegerField()
    content = models.CharField(max_length=255)
    books = models.ForeignKey(Book, related_name="reviews")
    users = models.ForeignKey(User, related_name="reviews")
    Created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()



