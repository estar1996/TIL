from django.urls import path
from . import views

# 커뮤니티 CRUD, 댓글 CRD
app_name = 'community'
urlpatterns = [
    path('', views.community_list_create, name='index'),
    path('<int:community_pk>/', views.community_detail, name='detail'),
    path('<int:community_pk>/comments/', views.comments, name='comments'),
    path('<int:community_pk>/comments/<int:comment_pk>/', views.comment_detail, name='comment_detail'),
]