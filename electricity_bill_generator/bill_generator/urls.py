from . import views
from django.urls import path

urlpatterns = [

    path('', views.generate_bill, name='generate_bill'),
    ]