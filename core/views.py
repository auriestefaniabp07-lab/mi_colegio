from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Section
from django.views import View

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

def register_student(request):
    return render(request, 'core/register_student.html')

class RegisterStudentCreateView(View):
    template_name = 'core/register_student.html'

    def get(self, request, *args, **kwargs):
        sections = Section.objects.all()
        return render(request, self.template_name, {'sections': sections})
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        lastname = request.POST.get("lastname")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        dni = request.POST.get("dni")
        gender = request.POST.get("gender")
        date_birth = request.POST.get("date_birth")
        direction = request.POST.get("direction")
        section_id = request.POST.get("section")
        section = Section.objects.filter(id= section_id).first() if section_id else None
        print(section)

        new_student = Student.objects.create(
            name=name,
            lastname=lastname,
            phone=phone,
            email=email,
            dni=dni,
            gender=gender,
            date_birth=date_birth,
            direction=direction,
            section=section
        )
        return redirect("estudiantes")

class StudentListView(View):
    template_name = 'core/estudiantes.html'

    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        return render(request, self.template_name, {'students': students})
    
class StudentDetailView(View):
    template_name = 'core/student_detail.html'

    def get(self, request, id, *args, **kwargs):
        student = get_object_or_404(Student, id=id)
        return render(request, self.template_name, {'s': student})
    
class StudentUpdateView(View):
    template_name = 'core/student_update.html'

    def get(self, request, id, *args, **kwargs):
        student = get_object_or_404(Student, id=id)
        sections = Section.objects.all()
        return render(request, self.template_name, {'student': student, 'sections': sections})
    
    def post(self, request, id, *args, **kwargs):
        student = get_object_or_404(Student, id=id)

        name = request.POST.get("name")
        lastname = request.POST.get("lastname")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        dni = request.POST.get("dni")
        gender = request.POST.get("gender")
        date_birth = request.POST.get("date_birth")
        direction = request.POST.get("direction")
        section_id = request.POST.get("section")
        section = Section.objects.filter(id=section_id).first() if section_id else None
        print(section)
        print(type(date_birth))

        student.name = name
        student.lastname = lastname
        student.phone = phone
        student.email = email
        student.dni = dni
        student.gender = gender
        student.date_birth = date_birth
        student.direction = direction
        student.section = section

        student.save()
        

        return redirect('estudiantes')

    
