# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *


def index(request):
    users = User.objects.all()
    context = {
        "all_user": users
    }
    return render(request, "user_restful/index.html", context)


def new(request):
    return render(request, "user_restful/new.html")


def create(request):
    valids = User.objects.basic_validator(request.POST)
    valid, stuff = valids
    if valid:
        pass
    else:
        messages.error(request,stuff)
    return redirect("/users/new")


def show(request, id):
    user = User.objects.get(id=int(id))
    context = {
        "user": user
    }
    return render(request, "user_restful/show.html", context)


def update(request, id):
    user = User.objects.get(id=int(id))
    context = {
        "user": user
    }
    return render(request, "user_restful/update.html", context)


def edit(request, id):
    valids = User.objects.basic_updater(request.POST, id)
    valid, stuff = valids
    if valid:
        pass
    else:
        messages.error(request, stuff)
    return redirect("/users/{}/update".format(id))

def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect("/users")























