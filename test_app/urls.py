from django.urls import path
from . import views

urlpatterns = [
    path('get_form', views.GetForm.as_view(), name='get_form'),
]
