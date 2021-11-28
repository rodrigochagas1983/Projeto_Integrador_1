from django.contrib import admin

from .models import EnderecoUbs, Especialidades, MedicoUbs, Senhas, Ubs, Agenda


class EnderecoUbsAdmin(admin.ModelAdmin):  # Classe usada para apresentar os dados formatados por tabela na interface admin
    list_display = ('rua', 'numero', 'bairro', 'cep', 'cidade', 'estado_uf', 'país')


admin.site.register(EnderecoUbs, EnderecoUbsAdmin)  # O que sera apresentado na listagem na interface admin


class EspecialidadesAdmin(admin.ModelAdmin):
    list_display = ['nome_especialidade']


admin.site.register(Especialidades, EspecialidadesAdmin)


class MedicoUbsAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')


admin.site.register(MedicoUbs, MedicoUbsAdmin)


class SenhasAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'senha')


admin.site.register(Senhas, SenhasAdmin)


class UbsAdmin(admin.ModelAdmin):
    list_display = ['nome_unidade']


admin.site.register(Ubs, UbsAdmin)


class AgendaUbsAdmin(admin.ModelAdmin):
    list_display = ('data_ag', 'horario_ag')


admin.site.register(Agenda, AgendaUbsAdmin)
