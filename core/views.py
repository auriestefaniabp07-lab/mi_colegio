from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def colegio2(request):
    return render(request, 'core/colegio2.html')

def colegio3(request):
    return render(request, 'core/colegio3.html')

def crearregistro(request):
    return render(request, 'core/crearregistro.html')

def docente_colegio(request):
    return render(request, 'core/docente_colegio.html')

def docente_colegio2(request):
    return render(request, 'core/docente_colegio2.html')

def materia_colegio(request):
    return render(request, 'core/materia_colegio.html')

def seccion_colegio(request):
    return render(request, 'core/seccion_colegio.html')