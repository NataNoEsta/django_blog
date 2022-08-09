from django.urls import path
from . import views
#from .views import PostList

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/post_list/', views.post_list, name="post_list"),
    #path('blog/post_list/', PostList.as_view(), name='post_list'), 

]