# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random


def index(request):
    if "total_gold" not in request.session:
        request.session["total_gold"] = 0

    if "activity_log" not in request.session:
        request.session["activity_log"] = []

    print request.session["total_gold"]
    return render(request, "gold_man_app/index.html")


def process(request):
    print "i am here at process"
    if request.POST["id_activity"] == "10":
        print "i am value 10"
        num = random.randrange(10, 20)
        request.session["total_gold"] += num
        request.session["activity_log"].append("you have earn " + str(num) + "$ at farm\n")

    elif request.POST["id_activity"] == "11":
        num = random.randrange(5, 10)
        request.session["total_gold"] += num
        request.session["activity_log"].append("you have earn " + str(num) + "$ at cave\n")

    elif request.POST["id_activity"] == "12":
        num = random.randrange(2, 5)
        request.session["total_gold"] += num
        request.session["activity_log"].append("you have earn " + str(num) + "$ at house\n")

    elif request.POST["id_activity"] == "13":
        num = random.randrange(-50, 51)
        request.session["total_gold"] += num
        if num > 0:
            request.session["activity_log"].append("you have earn " + str(num) + "$ at casino\n")
        elif num < 0:
            request.session["activity_log"].append("you have lost " + str(abs(num)) + "$ at casino\n")

    print request.session["total_gold"]
    request.session.modified = True

    return redirect("/")