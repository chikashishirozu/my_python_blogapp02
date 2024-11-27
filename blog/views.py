# blog/views.py
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.db.models import Q
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10  # ページネーションを使用する場合

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) | Q(text__icontains=query),
                published_date__isnull=False
            ).order_by('-id')    
        return Post.objects.filter(published_date__isnull=False).order_by('-id')  

def index(request):
    posts_list = Post.objects.filter(published_date__isnull=False).order_by('published_date')
    paginator = Paginator(posts_list, 10)  # 1ページに10件表示

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'blog/index.html', {'posts': posts})
    
def post_list(request):
    query = request.GET.get('q')
    posts = Post.objects.all()
    
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(text__icontains=query))
        return render(request, 'blog/post_list02.html', {'posts': posts, 'query': query})  # 検索結果がある場合のテンプレート
    
    return render(request, 'blog/post_list.html', {'posts': posts})
