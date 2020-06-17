from django.shortcuts import render, get_object_or_404 
from .models import Post, Category, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin 
from django.http import HttpResponse
from .forms import CommentForm


class CategoryList(ListView):
    model = Category
    queryset = Category.objects.all()
    context_object_name = 'categories'
    template_name = 'home.html'

    
class PostCategory(ListView):
    model = Post
    context_object_name = 'post_category'
    template_name  = 'blog/post/list.html'

    def get_queryset(self):
        return Post.objects.filter(category__slug= self.kwargs.get('slug'))
    

    
class PostDetail(FormMixin, DetailView):
    model = Post
    form_class = CommentForm
    context_object_name = 'post_detail'
    template_name = 'blog/post/detail.html'

    def post(self, request, *args, **kwargs):
        print('post')

    # def get_queryset(self):
    #     return Post.objects.filter(category__slug = self.kwargs.get('category'), slug = self.kwargs.get('slug'))

    # def get_success_url(self, *args, **kwargs):
    #     return reverse_lazy('post_detail', kwargs={'slug': self.get_object().slug})

    
def about(request):
    return HttpResponse('about.html')
