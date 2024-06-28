from django.contrib import admin
from .views import Sungla, About, Haqida, Carusel, Foydalanuvchi
from .models import Contact, Comment
# Register your models here.
admin.site.register(Contact)
@admin.register(Sungla)
class SunglaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Haqida)
class HaqidaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Carusel)
class CaruselAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user']

@admin.register(Foydalanuvchi)
class FoydalanuvchiAdmin(admin.ModelAdmin):
    list_display = ['ismi']