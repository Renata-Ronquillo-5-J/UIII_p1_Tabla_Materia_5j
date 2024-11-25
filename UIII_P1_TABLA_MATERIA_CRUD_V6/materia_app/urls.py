from django.urls import path 
from materia_app import views

urlpatterns = [
    path("vista_Materia",views.inicio_vista_Materia,name="vista_Materia"),
    path("registrarMateria/",views.registrarMateria,name="registrarMateria"),
    path("seleccionarMateria/<codigo>",views.seleccionarMateria,name="seleccionarMateria"),
    path("editarMateria/",views.editarMateria,name="editarMateria"),
    path("borrarMateria/<codigo>",views.borrarMateria,name="borrarMateria")
]
