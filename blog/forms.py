from django import forms
from .models import Post, Categoria

choices = Categoria.objects.all().values_list('nombre','nombre')
categorias = []
for c in choices:
    categorias.append(c)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'autor', 'entrada', 'categoria')

        widgets = {
                'titulo': forms.TextInput(attrs={'class': 'form-control'}),
                'autor':forms.TextInput(attrs={'class':'form-control','id':'name', 'value':' ', 'type':'hidden'}),
                'entrada': forms.Textarea(attrs={'class': 'form-control'}),
                'categoria': forms.Select(choices=categorias, attrs={'class': 'form-control'}),
            }

class EditForm(forms.ModelForm):
     class Meta:
        model = Post
        fields = ('titulo', 'entrada', 'categoria')

        widgets = {
                'titulo': forms.TextInput(attrs={'class': 'form-control'}),
                'entrada': forms.Textarea(attrs={'class': 'form-control'}),
                'categoria': forms.Select(choices=categorias, attrs={'class': 'form-control'}),
            }