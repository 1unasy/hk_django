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

# pk 같이 클라이언트가 서버에 보내는 데이터 : parameter
# post, posts 등 서버가 클라이언트에 보내는 데이터 : attribute
def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post' : post
        }
    )
