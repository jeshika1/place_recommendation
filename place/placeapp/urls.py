from django.urls import path
from placeapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('save/', views.save_preferences, name='save_preferences'),
]
