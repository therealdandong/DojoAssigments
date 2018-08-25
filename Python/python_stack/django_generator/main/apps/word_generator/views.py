# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
# Create your views here.


def index(request):
    if "counter" not in request.session:
        request.session["counter"] = 0
    else:
        request.session["counter"] += 1
    if "key_ran" not in request.session:
        request.session["key_ran"] = "abc"
    else:
        request.session["key_ran"] = get_random_string(length=14)
    context = {"key_ran": request.session["key_ran"]}
    print context["key_ran"]
    return render(request, "word_generator/index.html", context)


def reset(request):
    del request.session["counter"]
    print "hello i am here"
    return redirect("/")