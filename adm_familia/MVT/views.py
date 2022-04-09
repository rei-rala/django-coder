from django.shortcuts import render, get_object_or_404, redirect

from MVT.models import Person
from MVT.formsModel import PersonForm


def toPeople(request):
    return redirect("/people")


def people(request):
    template = "people/all.html"
    people = Person.objects.all()

    context = {
        "getObject": request.GET,
        "q_people": people.count(),
        "people": people,
    }

    return render(request, template, context)


def addPerson(request):
    template = "people/add.html"
    context = {}

    if request.method == "POST":
        postDictionary = request.POST.dict()
        postDictionary["relationship"] = 'Desconocido' if postDictionary["relationship"].replace(' ', '') == '' else postDictionary["relationship"]

        person = PersonForm(postDictionary)

        if person.is_valid():
            person.save()
            context["message"] = "Persona agregada correctamente"
        else:
            context["message"] = "Error al agregar persona"

    return render(request, template, context)


def editPerson(request, id):
    template = "people/edit.html"
    person = get_object_or_404(Person, pk=id)

    context = {"person": person, }

    if request.method == "POST":
        person = PersonForm(request.POST, instance=person)
        if person.is_valid():
            person.save()
            context["message"] = "Persona editada correctamente"
        else:
            context["message"] = "Error al editar persona"

    year, month, date = person.born.strftime("%Y-%m-%d").split('-')
    person.born = f'{str(year).ljust(4, "0")}-{month}-{date}'

    return render(request, template, context)


def deletePerson(request, id):
    template = "people/delete.html"
    context = {}

    person = get_object_or_404(Person, pk=id)
    context['person'] = person

    if request.method in ["POST", "DELETE"]:
        try:
            person.delete()
            context["message"] = "Persona eliminada correctamente"
        except Exception as e:
            context["message"] = f"Error al eliminar persona {e}"

    return render(request, template, context)
