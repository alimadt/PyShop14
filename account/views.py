
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import RegistrationForm


class RegisterView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')
