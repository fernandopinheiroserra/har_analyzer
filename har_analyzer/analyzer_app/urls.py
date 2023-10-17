from django.urls import path
from . import views

urlpatterns = [
    path('', views.analyze_har_view, name='analyze_har'),
]
