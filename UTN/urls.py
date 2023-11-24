from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('login/', views.login_view),
    path('signup/', views.signup),
    path('home/', views.home),
    path('historial/', views.historial),
    path('horario/', views.horario),
    path('inscribir/', views.inscribir),
    path('notas/', views.notas)
]