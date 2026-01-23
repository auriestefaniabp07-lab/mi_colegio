from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('colegio2', views.colegio2, name='colegio2'),
    path('colegio3', views.colegio3, name='colegio3'),
    path('crearregistro', views.crearregistro, name='crearregistro'),
    path('docente_colegio', views.docente_colegio, name='docente_colegio'),
    path('docente_colegio2', views.docente_colegio2, name='docente_colegio2'),
    path('materia_colegio', views.materia_colegio, name='materia_colegio'),
    path('seccion_colegio', views.seccion_colegio, name='seccion_colegio'),
    
]