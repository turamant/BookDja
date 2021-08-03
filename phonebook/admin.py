from django.contrib import admin

# Register your models here.
from phonebook.models import Phboo


@admin.register(Phboo)
class PhBodmin(admin.ModelAdmin):
    list_display = ('name', 'nomer', 'birthday', 'url')
    search_fields = ('name',)
    prepopulated_fields = {'url': ('name',)}
