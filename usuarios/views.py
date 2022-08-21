from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class RegistroUsuario(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'register/signup.html'
    success_url = reverse_lazy('login')