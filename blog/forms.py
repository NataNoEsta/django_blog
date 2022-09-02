from django import forms
from .models import Post
#Categoria

# choices = Categoria.objects.all().values_list('cat_name','cat_name')
# categorias = []
# for cat in choices:
#     categorias.append(cat)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'autor', 'entrada')

        widgets = {
                'titulo': forms.TextInput(attrs={'class': 'form-control'}),
                'autor':forms.TextInput(attrs={'class':'form-control','id':'name', 'value':' ', 'type':'hidden'}),
                'entrada': forms.Textarea(attrs={'class': 'form-control'}),
                # 'categoria': forms.Select(choices=categorias, attrs={'class': 'form-control'}),
            }

class EditForm(forms.ModelForm):
     class Meta:
        model = Post
        fields = ('titulo', 'entrada')

        widgets = {
                'titulo': forms.TextInput(attrs={'class': 'form-control'}),
                'entrada': forms.Textarea(attrs={'class': 'form-control'}),
                # 'categoria': forms.Select(choices=categorias, attrs={'class': 'form-control'}),
            }