from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'autor', 'entrada')

        widgets = {
                'titulo': forms.TextInput(attrs={'class': 'form-control'}),
                'autor':forms.TextInput(attrs={'class':'form-control','id':'name', 'value':' ', 'type':'hidden'}),
                'entrada': forms.Textarea(attrs={'class': 'form-control'}),
            }

class EditForm(forms.ModelForm):
     class Meta:
        model = Post
        fields = ('titulo', 'entrada')

        widgets = {
                'titulo': forms.TextInput(attrs={'class': 'form-control'}),
                'entrada': forms.Textarea(attrs={'class': 'form-control'}),
            }