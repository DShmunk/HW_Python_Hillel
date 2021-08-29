from django.urls import path
 
from .views import BlogCreateView, BlogListView, BlogDetailView
 
urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
    path('write', BlogCreateView.as_view(), name='post_form'),
]
