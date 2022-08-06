from django.urls import path
#from . import views
from blog.views import HomeView #se importa la clase HomeView como una vista desde views en la app blog

urlpatterns = [
    #path('',views.home, name='home'), # 
    path('', HomeView.as_view(), name='home'), 
]