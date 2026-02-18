from django.core.management.base import BaseCommand
from core.models import Section

class Command(BaseCommand):
    help = 'Sembrar datos iniciales en la base de datos de secciones'

    def handle(self, *args, **options):
        
        self.seed_sections()
    

    def seed_sections(self):
        sections = [ 
            {"letter_section": "A"},
            {"letter_section": "B"},
            {"letter_section": "C"},
        ]

        for section_data in sections:
            section, created = Section.objects.get_or_create(**section_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Sección "{section.letter_section}" creada exitosamente.'))
            else:
                self.stdout.write(self.style.WARNING(f'Sección "{section.letter_section}" ya existe.'))

    
