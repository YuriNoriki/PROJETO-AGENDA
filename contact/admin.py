from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    # Mostrando os campos no admin do django
    list_display = 'id','first_name', 'last_name', 'phone',
    # Para ficar na decrescente 
    ordering = '-id', 
    # list_filter = 'create_date',
    search_fields = 'id', 'first_name', 'last_name',
    # Exibir uma valor por pagina 
    list_per_page = 10
    # define o limite máximo de itens que podem ser exibidos ao clicar em "Mostrar todos" no Django Admin.
    list_max_show_all = 200
    # Campos que podem ser editaveis
    list_editable = 'first_name', 'last_name',

    # Fica como link para acessar
    list_display_links = 'id', 'phone',

@admin.register(models.Category)
class ContactAdmin(admin.ModelAdmin):
    # Mostrando os campos no admin do django
    list_display = 'name',
    # Para ficar na decrescente 
    ordering = '-id', 
 
