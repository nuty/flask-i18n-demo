# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, session


def lang():
    lang = request.args.get("lang", None)
    if lang:
        session["lang"] = lang
        return redirect("/")


def index():
    return render_template("index.html")