# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime


def index(req):
    context = {"time": strftime("%Y-%m-%d %H:%M %p", gmtime())}
    print(context["time"])
    return render(req, 'time_display/index.html', context)


