from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.index, name='index'),
    path('colegio2', views.colegio2, name='colegio2'),
    path('colegio3', views.colegio3, name='colegio3'),
    path('crearregistro', views.crearregistro, name='crearregistro'),
    path('docente_colegio', views.docente_colegio, name='docente_colegio'),
    path('docente_colegio2', views.docente_colegio2, name='docente_colegio2'),
    path('materia_colegio', views.materia_colegio, name='materia_colegio'),
    path('seccion_colegio', views.seccion_colegio, name='seccion_colegio'),
    path('register_student/', RegisterStudentCreateView.as_view(), name='register_student'),
    path('student/', StudentListView.as_view(), name='estudiantes'),
    path('student/<int:id>/', StudentDetailView.as_view(), name='student_detail'),
    path('students/<int:id>/update/', StudentUpdateView.as_view(), name='student_update'),
    path('students/<int:id>/delete/', StudentDeleteView.as_view(), name='student_delete'),
    path('register_teaching/', RegisterTeacherCreateView.as_view(), name='register_teaching')
]