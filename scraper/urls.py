from django.urls import path
from . import views

urlpatterns = [
    path('', views.scraper_home, name='scraper_home'),
    path('run/', views.scraper_run, name='scraper_run'),
]
