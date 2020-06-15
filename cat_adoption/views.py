from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class CatHomeView(TemplateView):
  template_name = 'cat_adoption.html'
