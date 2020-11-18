from trigrs.models import DataTrigrs, DataTrigrsDetail
from django import template
from django.utils import timezone
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from trigrs.forms import LoginForm
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout as auth_logout


@login_required(login_url="/login/")
def client_index(request):
    dataTrigrsCounter = ''
    fileUploadedCounter = ''

    try:
        data = DataTrigrs.objects.all()
    except DataTrigrs.DoesNotExist:
        data = None

    if data:
        dataTrigrsCounter = data.count()
    else:
        dataTrigrsCounter = 0

    try:
        data = DataTrigrsDetail.objects.filter(
            data_added__date=timezone.now().date())
    except DataTrigrsDetail.DoesNotExist:
        data = None

    if data:
        fileUploadedCounter = data.count()
    else:
        fileUploadedCounter = 0

    return render(request, "main/index.html", {"data_counter": dataTrigrsCounter, "file_uploaded": fileUploadedCounter})


def login_view(request):

    auth_logout(request)
    form = LoginForm(request.POST or None)

    msg = None

    if request.GET.get('message', '') == 'success':
        msg = 'Password berhasil diubah. Silakan login kembali dengan password baru'

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/dashboard/")
            else:
                msg = 'Username/password tidak valid'
        else:
            msg = 'Error validating the form'

    return render(request, "main/login.html", {"form": form, "msg": msg})


# -*- encoding: utf-8 -*-
"""
Copyright (c) 2020 - present BALAI LITBANG SABO
"""
