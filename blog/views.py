from django.shortcuts import render
from .models import Post

def index(request):

    # select * from Post; 와 동일 -> ORM
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        # django에서 알아서 /templates/를 앞에 붙여준다.
        'blog/index.html',
        {
            'posts' : posts
        }
    )
