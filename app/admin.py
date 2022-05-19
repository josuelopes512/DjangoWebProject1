from django.contrib import admin
from .models import Vacancies, UserClient, Candidato, Tecnologia
from django.contrib.admin import ModelAdmin

# Register your models here.


class VacanciesAdmin(ModelAdmin):
    model = Vacancies

class UserClientAdmin(ModelAdmin):
    model = UserClient

class CandidatoAdmin(ModelAdmin):
    model = Candidato

class TecnologiaAdmin(ModelAdmin):
    model = Tecnologia
    
admin.site.register(Vacancies, VacanciesAdmin)
admin.site.register(UserClient, UserClientAdmin)
admin.site.register(Candidato, CandidatoAdmin)
admin.site.register(Tecnologia, TecnologiaAdmin)
