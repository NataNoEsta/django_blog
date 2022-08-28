from django.views import generic
# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import CrearUsuario

class RegistroUsuario(generic.CreateView):
    form_class = CrearUsuario
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')