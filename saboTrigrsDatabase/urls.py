"""saboTrigrsDatabase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from trigrs.views import login_view, client_index, data_trigrs, add_data_trigrs

urlpatterns = [
    url(r'^login/',
        login_view, name='login-view'),
    url(r'^dashboard/',
        client_index, name='client-index'),
    url(r'^data-trigrs/',
        data_trigrs, name='data-trigrs'),
    url(r'^add-data-trigrs/',
        add_data_trigrs, name='add-data-trigrs'),
    url(r'^logout/', LogoutView.as_view(), name="logout"),
    url(r'^change-password/', auth_views.PasswordChangeView.as_view(
        template_name='main/change-password.html',
        success_url='/login/?message=success'
    ),
        name='change-password'
    ),
]
