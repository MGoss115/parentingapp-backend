from django.urls import path
from . import views

urlpatterns = [
    path('', views.kid_form, name='kid_form')
]
