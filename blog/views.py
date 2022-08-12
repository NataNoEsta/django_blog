#from django.shortcuts import render, HttpResponse #funciones
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

#View basada en funiones correspondiente a 'home.html'
#View basada en clases

class HomeView(TemplateView):
    model = Post
    template_name = 'home.html'

class PostList(ListView):
    model = Post
    template_name = 'blog.html'
    ordering = ['fecha_publicacion']

class EntryView(DetailView):
    model = Post
    template_name = 'entry.html'