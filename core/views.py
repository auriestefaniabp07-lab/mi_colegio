from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def colegio2(request):
    return render(request, 'core/colegio2.html')