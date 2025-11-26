from django.urls import path
from . import views

urlpatterns = [
    path('', views.alumno_list, name='alumno_list'),
    path('<int:pk>/', views.alumno_detail, name='alumno_detail'),
    path('crear/', views.alumno_create, name='alumno_create'),
    path('<int:pk>/editar/', views.alumno_update, name='alumno_update'),
    path('<int:pk>/eliminar/', views.alumno_delete, name='alumno_delete'),
    path('<int:pk>/pdf/', views.alumno_pdf, name='alumno_pdf'),
]


