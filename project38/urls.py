"""
URL configuration for project38 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Fbvstring/',Fbvstring,name='Fbvstring'),
    path('Fbvhtml/',Fbvhtml,name='Fbvhtml'),
    path('Cbvhtml/',Cbvhtml.as_view(),name='Cbvhtml'),
    path('Cbvstring/',Cbvstring.as_view(),name='Cbvstring'),
    path('insert_cbv/',insert_cbv.as_view(),name='insert_cbv')

]
