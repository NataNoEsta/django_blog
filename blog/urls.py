from django.urls import path
from . import views
from .views import HomeView, PostList, EntryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    #path('blog/post_list/', views.post_list, name="post_list"),
    path('blog/', PostList.as_view(), name='blog'), 
    path('blog/entry/<int:pk>', EntryView.as_view(), name='entry'),

]