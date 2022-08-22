#from django.shortcuts import render, HttpResponse #funciones
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import PostForm, EditForm
from .models import Post
from django.shortcuts import render, redirect

#View basada en funciones correspondiente a 'home.html'
#View basada en clases

def homeView(request):
    return render(request, 'home.html')

def acercaView(request):
    return render(request, 'acerca.html')

def contactoView(request):
    return render(request, 'contacto.html')

def campañasView(request):
    return render(request, 'campañas.html')

class PostList(ListView):
    model = Post
    template_name = 'blog.html'
    ordering = ['-fecha_publicacion']
    paginate_by = 2

class EntryView(DetailView):
    model = Post
    template_name = 'entry.html'

class AddPost(CreateView):
    form_class = PostForm
    template_name = 'add_post.html'

class EditPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'