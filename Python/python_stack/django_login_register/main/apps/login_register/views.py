# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


def index(request):
    return render(request, "login_register/index.html")


def success(request, id):
    user = User.objects.get(id=id)
    context = {
        "user": user
    }
    return render(request, "login_register/success.html", context)


def process(request):
    valids = User.objects.basic_validator(request.POST)
    valid, stuff = valids
    if valid:
        pass
    else:
        messages.error(request, stuff)
    return redirect("/")


def validate(request):
    valids = User.objects.login_checker(request.POST)
    valid, stuff = valids
    if valid:
        return redirect("/success/{}".format(stuff.id))
    else:
        messages.error(request, stuff)
    return redirect("/")
