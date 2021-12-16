from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# '목록'을 보여주는 개념(ListView)에 알맹이(Post)를 넣겠다.
class PostList(ListView):
    # post_list 를 만든다.
    # -> urls.py의 as_view() 함수기 post 목록을 다 가져온다.
    model = Post
    
    # 장고의 ListView에서 자동으로 지정하는
    # post_list.html을 사용하지 않고, index.html을 사용
    # template_name = "blog/index.html"

    # 데이터 조회 정렬하기(내림차순)
    ordering = "-pk"

class PostDetail(DetailView):
    model = Post


# def index(request):
#
#     # select * from Post; 와 동일 -> ORM
#     posts = Post.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         # django에서 알아서 /templates/를 앞에 붙여준다.
#         'blog/index.html',
#         {
#             'posts' : posts
#         }
#     )

# pk 같이 클라이언트가 서버에 보내는 데이터 : parameter
# post, posts 등 서버가 클라이언트에 보내는 데이터 : attribute
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post' : post
#         }
#     )
