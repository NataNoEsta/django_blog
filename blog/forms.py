from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'autor', 'entrada')

        widgets = {
                'titulo': forms.TextInput(attrs={'class': 'form-control'}),
                'autor':forms.Select(attrs={'class':'form-control'}),
                'entrada': forms.Textarea(attrs={'class': 'form-control'}),
            }