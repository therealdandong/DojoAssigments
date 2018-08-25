# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


def index(request):
    return render(request, "amadon_buy/index.html")


def result(request):
    return render(request, "amadon_buy/result.html")


def process(request):
    if request.POST["product_id"] == "1234":
        request.session["price_spend"] = 19.99
    if request.POST["product_id"] == "2345":
        request.session["price_spend"] = 29.99
    if request.POST["product_id"] == "3456":
        request.session["price_spend"] = 9.99
    if request.POST["product_id"] == "4567":
        request.session["price_spend"] == 49.99
    return redirect("/amadon/result")
