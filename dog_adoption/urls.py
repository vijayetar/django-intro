from django.urls import path
from .views import DogHomeView

urlpatterns = [
  path('',DogHomeView.as_view(), name="doggy_home"),
]