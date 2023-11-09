from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Setup

def home(request):
  return render(request, 'home.html')

class SignUpView(generic.CreateView):
  form_class = CustomUserCreationForm
  success_url = reverse_lazy('login') # Redirect to login page after signup
  template_name = 'registration/signup.html'

class AddSetupView(LoginRequiredMixin, TemplateView):
  template_name = 'add_setup.html'
  login_url = '/login/'
  
class FavoritesView(LoginRequiredMixin, ListView):
  model = Setup
  template_name = 'favorites.html'
  context_object_name = 'favorites'
  
  def get_queryset(self):
    return self.request.user.favorites.all()