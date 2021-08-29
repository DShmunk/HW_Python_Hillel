# Create your views here.

from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
 

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'post_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
 
class BlogListView(ListView):
    model = Post
    paginate_by = 3
    template_name = 'home.html'
    
        
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
