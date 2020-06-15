from django.urls import path
from .views import CatHomeView

urlpatterns = [
  path('',CatHomeView.as_view(), name="cat_home"),
]