# blog app에서 사용할 url을 등록
from django.urls import path
from . import views

urlpatterns = [
    # <ip: port>/blog : 블로그 메인 페이지
    # - 이미 hk_django_prj의 urls.py에 블로그에 들어가는 url 적어놓았기 때문 (포스트 목록 = 블로그 메인 p.161)
    # 도메인/blog/포스트 pk -> 포스트 pk = blog APP
    # 블로그 앱에 아무것도 안 치고 들어오면 views.index 함수를 보여줄거야.
    path('', views.index),

]