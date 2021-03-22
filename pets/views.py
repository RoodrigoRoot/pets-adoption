from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pet

# Create your views here.

class PetsListView(ListView):
    model = Pet
    template_name = "pets/list-pets.html"


class PetDetailView(LoginRequiredMixin, DetailView):
    model = Pet
    template_name = "pets/pet-detail.html"
    lookup_field = "slug"
