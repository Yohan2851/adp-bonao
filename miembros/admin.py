from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from .models import User
from django.contrib.auth.models import Group

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    fieldsets  =  (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'last_name', 'email', 'picture')}),
        ('Información Adicional', {'fields': ('cedula', 'telefono', 'estado_civil', 'direccion', 'codigo_de_cuenta')}),
        ('Ubicación', {'fields': ('distrito', 'escuela')}),
        ('Cargo', {'fields': ('cargo',)}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'date_joined')



