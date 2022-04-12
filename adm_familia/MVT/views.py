from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView

from MVT.models import Person, Movie, Brand
from MVT.formsModel import PersonForm, MovieForm, BrandForm


def to_html_date(date_like) -> str:
    temp_date = date_like

    if type(date_like) == str:
        temp_date = datetime.strptime(date_like, "%Y-%m-%d")

    year, month, date = temp_date.strftime("%Y-%m-%d").split("-")

    return f'{str(year).ljust(4, "0")}-{month}-{date}'


def toPeople(request):
    return redirect("/people")


class NewX(TemplateView):
    template_name = "_general/add.html"

    def get(self, request):
        return render(request, self.template_name)


class BrandAdd(TemplateView):
    template_name = "brands/add.html"

    def post(self, request):
        message = None
        form = BrandForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                message = "La marca se ha guardado correctamente"
            else:
                message = "Error. Verifique los datos ingresados."
        except Exception as e:
            message = f"Ha ocurrido un error: {e}"

        return render(request, self.template_name, {"form": form, "message": message})


class MovieAdd(TemplateView):
    template_name = "movies/add.html"

    def post(self, request):
        message = None
        form = MovieForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                message = "La marca se ha guardado correctamente"
            else:
                message = "Error. Verifique los datos ingresados."
        except Exception as e:
            message = f"Ha ocurrido un error: {e}"

        return render(request, self.template_name, {"form": form, "message": message})


class PersonSearch(TemplateView):
    template_name = "people/search.html"
    model_fields = Person._meta.get_fields()
    model_field_names = [field.name for field in model_fields]

    """ for a in model_fields:
        print(a.name) """

    context = {
        "default_born_date": to_html_date(datetime.now()),
        "model_fields": [
            {"name":f.name, 'type':f.get_internal_type, "is_relation": f.is_relation} for f in model_fields
        ],
    }

    def get(self, request):
        print(self.model_fields[4].is_relation)

        return render(request, self.template_name, self.context)

    def post(self, request):
        search_term = request.POST.get("search_term")
        search_value = request.POST.get("search_value")
        search_strict = request.POST.get("search_strict") == "on"

        if search_term in self.model_field_names:
            idx = self.model_field_names.index(search_term)
            query = None
            if self.model_fields[idx].is_relation:
                # TODO: query including Foreign Keys!
                query = {f"{search_term}__{'exact' if search_strict else 'exact' or 'contains' }": search_value if type(search_value) == int else 0}
            else:
                query = {f"{search_term}__{'exact' if search_strict else 'contains' }": search_value}

            self.context["people"] = Person.objects.filter(**query)

        self.context = {
            **self.context,
            "people_count": self.context['people'].count(),
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


class PersonAdd(TemplateView):
    template = "people/add.html"
    context = {
        "default_born_date": to_html_date(datetime.now()),
    }
    message = None

    def get(self, request):
        movies = Movie.objects.all()
        brands = Brand.objects.all()

        self.context = {
            **self.context,
            "movies": movies,
            "brands": brands,
            "q_movies": movies.count(),
            "q_brands": brands.count(),
        }

        return render(request, self.template, self.context)

    def post(self, request):
        person = PersonForm(request.POST)

        if person.is_valid():
            person.save()
            self.message = "Persona agregada correctamente."
        else:
            self.message = "Error al agregar persona, verifique los datos ingresados."

        return redirect("addPerson")


class PersonEdit(TemplateView):
    template = "people/edit.html"

    def get(self, request, id):
        person = get_object_or_404(Person, pk=id)
        person.born = to_html_date(person.born)
        movies = Movie.objects.all()
        brands = Brand.objects.all()

        context = {
            "person": person,
            "movies": movies,
            "brands": brands,
            "q_movies": movies.count(),
            "q_brands": brands.count(),
        }
        return render(request, self.template, context)

    def post(self, request, id):
        person = get_object_or_404(Person, pk=id)
        context = {}
        try:
            editedPerson = PersonForm(request.POST, instance=person)

            movies = Movie.objects.all()
            brands = Brand.objects.all()

            context = {
                "person": person,
                "movies": movies,
                "brands": brands,
                "q_movies": movies.count(),
                "q_brands": brands.count(),
            }
            if editedPerson.is_valid():
                editedPerson.save()

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
