from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout
# Create your views here.


def logout_user(request):
    logout(request)
    return redirect("pets/")