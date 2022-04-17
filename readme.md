# Django test: Proyecto

## Modelo MVT

Pasos para correr este proyecto

1. Ve a un directorio a eleccion.
1. Clona este repositorio con `git clone https://github.com/rei-rala/django-coder`.
1. _(A eleccion)_ Crea un entorno virtual para Python y activalo.
1. Instala los requirements `pip install -r requirements.txt`.
1. Corre el servidor con `python manage.py runserver`. <sub><sup>manage.py se encuentra en carpeta de proyecto /adm_familia</sub></sup>.
1. Ve a la direccion IP que se muestre por consola.

---

## Paths

Metodo: _GET_
Nota: Los _ID_ son numericos

### Base

> **root** o **"/"**: _Redireccion_ a /people

### People

> **/people**:  Muestra lista de personas
>
> **/people/search**:  Busqueda de personas
>
> **/people/person/**`...`
>
> - `...`/**add**: Agrega nueva persona
>
> - `...`/**edit/`ID_Persona`**: Edita una persona segun su ID
>
> - `...`/**delete/`ID_Persona`**

### Brand

> **/brand/**`...`
>
> - `...`**/add**: Añade nueva marca

### Movie

> **/movie/**`...`
>
> - `...`/**add**: Añade nueva pelicula

---
