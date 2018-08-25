# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

print "i am in view"


def index(request):
    context = {
        "name": "jason",
        "email": "jason@gmail.com"
    }
    return render(request, "first_blog/index.html", context)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)


def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = 'test'
        print "*"*50
        return redirect("/")
    else:
        return redirect("/")


def show(request,number):
    response = "placeholder to blog {}".format(number)
    return HttpResponse(response)


def edit(request,number):
    response = "placeholder to blog {} to edit".format(number)
    return HttpResponse(response)


def delete(request, number):
    return redirect("/")