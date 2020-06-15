from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class DogHomeView(TemplateView):
  template_name='dog_adoption.html'
