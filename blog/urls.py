from django.urls import path
from . import views
from .views import PostList, EntryView

urlpatterns = [
    #path('', HomeView.as_view(), name='home'),
    path('', views.homeView, name='home'),
    path('blog/', PostList.as_view(), name='blog'), 
    path('blog/entry/<int:pk>', EntryView.as_view(), name='entry'),
    path('acerca/', views.acercaView, name='acerca'),

]