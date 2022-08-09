from django.shortcuts import render, HttpResponse #funciones
#from django.views.generic import ListView
#clases | views genericas de django
from .models import Post
from django.template import loader

#View basada en funiones correspondiente a 'home.html'
def home(request):
    return render(request, "home.html",{})

def post_list(request):
    posts = Post.objects.all()
    template = loader.get_template('post_list.html')
    context = {
        'posts': posts,
        }
    return HttpResponse(template.render(context, request))

#View basada en clases
# class PostList(ListView):
#      model = Post
#      template_name = 'post_list.html'