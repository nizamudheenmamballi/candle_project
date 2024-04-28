from django.urls import path
from . import views

urlpatterns = [
    path('candles/', views.candles, name='candles'),
]