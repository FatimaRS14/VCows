from django.urls import path
from .import views

urlpatterns = [
    path('vacas/', views.cows, name="vacas"),
    path('toros/', views.cows, name="toros"),
]