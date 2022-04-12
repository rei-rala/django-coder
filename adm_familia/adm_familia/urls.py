"""adm_familia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from MVT.views import toPeople, PersonSearch, PersonEdit, PersonList, PersonFormAdd, PersonDelete

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", toPeople, name='root'),
    path("people/", PersonList.as_view(), name='people'),
    path('people/search', PersonSearch.as_view(), name='searchPerson'),
    path('people/person/add/', PersonFormAdd.as_view(), name='addPerson'),
    path('people/person/edit/<int:id>', PersonEdit.as_view(), name='editPerson'),
    path('people/person/delete/<int:id>', PersonDelete.as_view(), name='deletePerson'),
]
