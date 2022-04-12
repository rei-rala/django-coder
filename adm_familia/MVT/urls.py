from django.urls import path
from MVT.views import (
    toPeople,
    PersonSearch,
    PersonEdit,
    PersonList,
    PersonAdd,
    PersonDelete,
    BrandAdd,
    MovieAdd,
    NewX,
)


urlpatterns = [
    path("", toPeople, name="root"),
    path("add/", NewX.as_view(), name="new"),
    path("people/", PersonList.as_view(), name="people"),
    path("people/search", PersonSearch.as_view(), name="searchPerson"),
    path("people/person/add/", PersonAdd.as_view(), name="addPerson"),
    path("people/person/edit/<int:id>/", PersonEdit.as_view(), name="editPerson"),
    path("people/person/delete/<int:id>/", PersonDelete.as_view(), name="deletePerson"),
    path("brand/add/", BrandAdd.as_view(), name="addBrand"),
    path("movie/add/", MovieAdd.as_view(), name="addMovie"),
]
