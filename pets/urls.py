from django.urls import path
from .views import PetsListView, PetDetailView

urlpatterns = [
    path("pets/", PetsListView.as_view(), name="pets"),
    path("pets/<slug:slug>/", PetDetailView.as_view(), name="pet-detail"),
]
