from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Section, Student, Subject, Teaching, TeachingSection, StudentSubject

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Section)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Teaching)
admin.site.register(TeachingSection)
admin.site.register(StudentSubject)