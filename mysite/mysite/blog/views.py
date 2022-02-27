from django.shortcuts import render
from django.views import generic
from .models import Post
# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class CreatePost(generic.CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'slug', 'author', 'content', 'status']
    success_url = '/'

class DeletePost(generic.DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = '/'
    

class UpdatePost(generic.UpdateView):
    model = Post
    template_name = 'post_form.html'
    success_url = '/'
    fields = ['title', 'slug', 'content', 'status']

def about_page(request):
    return render(request, "about.html")
