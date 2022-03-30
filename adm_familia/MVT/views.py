from django.shortcuts import render

from MVT.models import Persona


def mvtHome(request):
    template = "home.html"
    people = Persona.objects.all()

    context = {
        "getObject": request.GET,
        "cantidad_personas": people.count(),
        "personas": people,
    }

    return render(request, template, context)
