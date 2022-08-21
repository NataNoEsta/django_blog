from django.urls import path
from .views import RegistroUsuario

urlpatterns = [
    path('signup/', RegistroUsuario.as_view(), name='signup'),
]