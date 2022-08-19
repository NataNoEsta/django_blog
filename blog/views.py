#from django.shortcuts import render, HttpResponse #funciones
from django.views.generic import ListView, DetailView, CreateView
from django.utils import timezone
from .forms import PostForm
from .models import Post
from django.shortcuts import render, redirect

#View basada en funiones correspondiente a 'home.html'
#View basada en clases

def homeView(request):
    return render(request, 'home.html')

def acercaView(request):
    return render(request, 'acerca.html')

class PostList(ListView):
    model = Post
    template_name = 'blog.html'
    ordering = ['fecha_publicacion']

class EntryView(DetailView):
    model = Post
    template_name = 'entry.html'

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'