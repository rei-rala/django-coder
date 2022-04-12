from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView

from MVT.models import Person
from MVT.formsModel import PersonForm


def to_html_date(date_like) -> str:
    temp_date = date_like

    if type(date_like) == str:
        temp_date = datetime.strptime(date_like, "%Y-%m-%d")

    year, month, date = temp_date.strftime("%Y-%m-%d").split("-")

    return f'{str(year).ljust(4, "0")}-{month}-{date}'


def toPeople(request):
    return redirect("/people")


class PersonSearch(TemplateView):
    template_name = "people/search.html"
    
    context = {
        "default_born_date": to_html_date(datetime.now()),
        "model_fields": [str(h).split('.')[2].replace('&#x27;', '') for h in Person._meta.get_fields()],
    }

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        search_term = request.POST.get("search_term")
        search_value = request.POST.get("search_value")
        search_strict = request.POST.get("search_strict") == 'on'

        query = Person.objects.filter(**{f"{search_term}__{'exact' if search_strict else 'contains' }": search_value})

        self.context = {
            **self.context,
            "people": query,
            "people_count": query.count(),
            "search_term": search_term,
            "search_value": search_value,
            "search_strict": search_strict,
        }
        
        return render(request, self.template_name, self.context)


class PersonList(TemplateView):
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
    context = {"default_born_date": to_html_date(datetime.now())}

    def get(self, request):
        return render(request, self.template, self.context)

    def post(self, request):
        postDictionary = request.POST.dict()

        postDictionary["relationship"] = (
            "Desconocido"
            if postDictionary["relationship"].strip() == ""
            else postDictionary["relationship"].strip()
        )

        person = PersonForm(postDictionary)
        self.context["person"] = person

        if person.is_valid():
            person.save()
            self.context["message"] = "Persona agregada correctamente."
        else:
            self.context[
                "message"
            ] = "Error al agregar persona, verifique los datos ingresados."

        return render(request, self.template, self.context)


class PersonEdit(TemplateView):
    template = "people/edit.html"

    def get(self, request, id):
        person = get_object_or_404(Person, pk=id)
        person.born = to_html_date(person.born)
        context = {"person": person}

        return render(request, self.template, context)

    def post(self, request, id):
        context = {}
        person = get_object_or_404(Person, pk=id)
        try:
            person.born = to_html_date(person.born)
            context["person"] = person.__dict__

            form = PersonForm(request.POST, instance=person)

            if form.is_valid():
                form.save()
                context["message"] = "Persona editada correctamente"
            else:
                context[
                    "message"
                ] = "Error al editar persona, verifique los datos ingresados"
        except Exception as e:
            context["message"] = f"Error al editar persona. \n{e}"

        return render(request, self.template, context)


class PersonDelete(TemplateView):
    template = "people/delete.html"

    def get(self, request, id):
        person = get_object_or_404(Person, pk=id)

        person.born = to_html_date(person.born)
        context = {"person": person}

        return render(request, self.template, context)

    def post(self, request, id):
        person = get_object_or_404(Person, pk=id)

        person.born = to_html_date(person.born)
        context = {"person": person}

        try:
            person.delete()
            context["message"] = "Persona eliminada correctamente"
        except Exception as e:
            context["message"] = f"Error al eliminar persona.\n {e}"

        return render(request, self.template, context)

    def delete(self, request, id):
        person = get_object_or_404(Person, pk=id)

        person.born = to_html_date(person.born)
        context = {"person": person}

        try:
            person.delete()
            context["message"] = "Persona eliminada correctamente"
        except Exception as e:
            context["message"] = f"Error al eliminar persona.\n {e}"

        return render(request, self.template, context)
