from django.contrib import admin
from .models import Pet
from .models import PetsVaccine
# Register your models here.

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):

    list_display = ["name", "breed", "age"]    
    search_fields = ["name", "breed", "age"]
    list_filter = ["age"]
    readonly_fields = ("slug",)


@admin.register(PetsVaccine)
class PetsVaccineAdmin(admin.ModelAdmin):
    
    list_display = ["pet", "vaccine"]
    list_filter = ["date"]
