from django.urls import path
from .views import RegistroUsuario

URLPATTERNS = [
    path('signup/', RegistroUsuario.as_view(), name='signup'),
]