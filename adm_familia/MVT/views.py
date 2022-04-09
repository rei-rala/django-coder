from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView

from MVT.models import Person
from MVT.formsModel import PersonForm


def toPeople(request):
    return redirect("/people")


class PersonListView(TemplateView):
    def get(self, request):
        template_name = "people/all.html"
        people = Person.objects.all()
        context = {
            "getObject": request.GET,
            "q_people": people.count(),
            "people": people,
        }
        return render(request, template_name, context)


class PersonFormAdd(TemplateView):
    template = "people/add.html"

    def get(self, request):
        return render(request, self.template, {})

    def post(self, request):
        context = {}

        postDictionary = request.POST.dict()
        postDictionary["relationship"] = 'Desconocido' if postDictionary["relationship"].replace(
            ' ', '') == '' else postDictionary["relationship"]

        person = PersonForm(postDictionary)

        if person.is_valid():
            person.save()
            context["message"] = "Persona agregada correctamente"
        else:
            context["message"] = "Error al agregar persona"

        return render(request, self.template, context)


class PersonEdit(TemplateView):
    context = {}
    template = "people/edit.html"

    def get(self, request, id):
        person = get_object_or_404(Person, pk=id)
        self.context = {"person": person, }
        return render(request, self.template, self.context)

    def post(self, request, id):
        person = get_object_or_404(Person, pk=id)
        person = PersonForm(request.POST, instance=person)

        if person.is_valid():
            person.save()
            self.context["message"] = "Persona editada correctamente"
        else:
            self.context["message"] = "Error al editar persona"

        year, month, date = person.born.strftime("%Y-%m-%d").split('-')
        person.born = f'{str(year).ljust(4, "0")}-{month}-{date}'

        return render(request, self.template, self.context)


class PersonDelete(TemplateView):
    template = "people/delete.html"
    context = {}

    def get(self, request, id):
        person = get_object_or_404(Person, pk=id)
        self.context = {"person": person, }
        return render(request, self.template, self.context)

    def post(self, request, id):
        person = get_object_or_404(Person, pk=id)
        try:
            person.delete()
            self.context["message"] = "Persona eliminada correctamente"
        except Exception as e:
            self.context["message"] = f"Error al eliminar persona, {e}"

        return render(request, self.template, self.context)

    def delete(self, request, id):
        person = get_object_or_404(Person, pk=id)
        try:
            person.delete()
            self.context["message"] = "Persona eliminada correctamente"
        except Exception as e:
            self.context["message"] = f"Error al eliminar persona, {e}"

        return render(request, self.template, self.context)
