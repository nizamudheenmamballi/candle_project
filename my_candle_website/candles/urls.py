from django.urls import path
from . import views

urlpatterns = [
    path('candles/', views.candles, name='candles'),
    path('stick/', views.stick, name='stick'),
    # path('', views.stick, name='candles'),
]