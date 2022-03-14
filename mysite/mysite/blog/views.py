from django.shortcuts import render
from django.views import generic
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class CreatePost(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'slug', 'author', 'content', 'status', 'image']
    success_url = '/'

class DeletePost(LoginRequiredMixin, generic.DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = '/'
    

class UpdatePost(LoginRequiredMixin, generic.UpdateView):
    model = Post
    template_name = 'post_form.html'
    success_url = '/'
    fields = ['title', 'slug', 'content', 'status', 'image']

def about_page(request):
    return render(request, "about.html")

class ListPost(LoginRequiredMixin, generic.ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name = 'post_list.html'