from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

# ------------------------------------------------------
# Usuario
# ------------------------------------------------------
class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = ["phone_number"]

    class Meta:
        db_table = "users"
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f"{self.username} ({self.email})"
    
# ------------------------------------------------------
# Sección
# ------------------------------------------------------
class Section(models.Model):
    letter_section = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'sections'
        verbose_name = 'Seccion'
        verbose_name_plural = 'Secciones'
    
    def __str__(self):
        return f"{self.letter_section}"
    

# ------------------------------------------------------
# Estudiante
# ------------------------------------------------------
class Student(models.Model):
    section = models.ForeignKey(Section, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    dni = models.CharField(max_length=8, null=True, unique=True)
    gender = models.CharField(max_length=50, null=True)
    date_birth = models.DateField()
    direction = models.TextField(null=True)
    class Meta:
        db_table = 'students'
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

    def __str__(self):
        return f"{self.name} ({self.dni})"

# ------------------------------------------------------
# Materia
# ------------------------------------------------------
class Subject(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(
        verbose_name='Descripción detallada', max_length=500, blank=True, null=True)
    image = models.ImageField(
        verbose_name='Imagen',
        upload_to='core/subject/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])],
        blank=True,
        null=True
    )
    class Meta:
        db_table = 'subjects'
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'

    def __str__(self):
        return f"{self.name} ({self.description})"
    
    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        super().delete(*args, **kwargs)

# ------------------------------------------------------
# Docente
# ------------------------------------------------------
class Teaching(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    direction = models.TextField(null=True)
    specialty = models.CharField(max_length=100)

    class Meta:
        db_table = 'teachers'
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'

    def __str__(self):
        return f"{self.name} ({self.lastname})"

# ------------------------------------------------------
# Docente_sección
# ------------------------------------------------------
class TeachingSection(models.Model):
    teaching = models.ForeignKey(Teaching, on_delete=models.PROTECT)
    section = models.ForeignKey(Section, on_delete=models.PROTECT)

    class Meta:
        db_table = 'teachers_sections'
        unique_together = [['teaching', 'section']]

    def __str__(self):
        return f"{self.teaching.name} imparte {self.section.name} "

# ------------------------------------------------------
# Estudiante_Materia
# ------------------------------------------------------
class StudentSubject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)

    class Meta:
        db_table = 'students_subjects'
        unique_together = [['student', 'subject']]

    def __str__(self):
        return f"{self.student.name} inscrito en {self.subject.name} "