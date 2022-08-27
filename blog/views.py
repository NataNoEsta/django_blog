from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm
from .models import Categoria, Post
from django.shortcuts import render
from django.urls import reverse_lazy, reverse

#View basada en funciones correspondiente a 'home.html'
#View basada en clases

def homeView(request):
    return render(request, 'home.html')

def acercaView(request):
    return render(request, 'acerca.html')

def contactoView(request):
    return render(request, 'contacto.html')

def accionesView(request):
    return render(request, 'acciones.html')

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

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCategoria(CreateView):
    model = Categoria
    template_name = 'add_categoria.html'
    fields = '__all__'

def CategoriasView(request, categoria):
    categoria_posts = Post.objects.filter(categoria=categoria.replace('-',' '))
    return render(request, 'categorias.html', {'categoria':categoria, 'categoria_posts':categoria_posts})