from django.shortcuts import render #funciones
from django.views.generic import TemplateView #clases | views genericas de django

# Create your views here. 
#View basada en funiones correspondiente a 'home.html'
# def home(request):
#     return render(request, "home.html",{})

#View basada en clases
class HomeView(TemplateView):
     template_name = 'home.html'