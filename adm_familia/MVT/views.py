from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render


def mvtHome(request):
    context = { "query": request.GET }
    return render(request, "./templates/home.html", context)
