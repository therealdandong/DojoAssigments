# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


def index(request):

    return render(request, 'survery/index.html')


def result(request):
    return render(request, 'survery/result.html')


def process(request):
    request.session["name"] = request.POST["name"]
    request.session["location"] = request.POST["location"]
    request.session["language"] = request.POST["language"]
    request.session["comment"] = request.POST["comment"]

    if "counter" not in request.session:
        request.session["counter"] = 0
    else:
        request.session["counter"] += 1
    return redirect("/result")