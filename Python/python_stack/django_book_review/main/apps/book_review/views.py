# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    return render(request, "book_review/index.html")


def process_register(request):
    valids = User.objects.basic_validator(request.POST)
    valid, result = valids
    if valid:
        messages.info(request, result)
    else:
        messages.error(request, result)
    return redirect("/")


def process_login(request):
    valids = User.objects.login_check(request.POST)
    valid, result = valids
    if valid:
        request.session["id"] = result.id
        return redirect("/users/{}".format(result.id))
    else:
        messages.error(request, result)
        return redirect("/")


def users(request, id):
    user = User.objects.get(id=id)
    context = {
        "user": user
    }
    return render(request, "book_review/user_review.html", context)


def add_all(request):

    authors = Author.objects.all()
    context = {
        "authors": authors,
    }
    return render(request, "book_review/add_all.html", context)


def add_all_process(request):
    print("i am in process")

    valid_author, result_author = Author.objects.valida_author(request.POST)
    print valid_author
    if not valid_author:
        messages.error(request, result_author)
        return redirect("/books/add")

    valid_book, result_book = Book.objects.valida_book(request.POST)
    if not valid_book:
        messages.error(request, result_book)
        return redirect("/books/add")

    valid_review, result_review = Review.objects.valida_review(request.POST)
    if not valid_review:
        messages.error(request, result_review)
        return redirect("/book/add")
    reviews, rating = result_review

    author_new = Author.objects.create(name=result_author)
    book_new = Book.objects.create(title=result_book, author=author_new)
    Review.objects.create(star=rating, content=reviews, books=book_new,
                          users=User.objects.get(id=request.session["id"]))

    return redirect("/books/{}".format(book_new.id))


def add_book(request,id):
    book = Book.objects.get(id=id)
    total_review = book.objects.reviews.all()
    if len(total_review) > 3:
        total_review = book.objects.review.all().order_by("Created_at")[:3]
    context = {
        "total_review": total_review
    }
    return render(request,"book_review/add_book.html",context)















