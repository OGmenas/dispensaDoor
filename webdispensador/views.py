from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,"webdispensador")

from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView

from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import User


