# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import Blog

def index(request):
    return render(request, "blog_test/index.html")


def update(request):
    errors = Blog.objects.basic_validator(request.POST)

    if len(errors):
        for tag, error in errors.iteritems():
            messages.error=(request, error, tag)
        return redirect('/blog/edit/'+id)
    else:
        blog = Blog.objects.get(id=id)
        blog.name = request.POST['name']
        blog.name = request.POST['desc']
        blog.save()
        return redirect('/blogs')