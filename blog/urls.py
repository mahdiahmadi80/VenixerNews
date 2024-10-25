from django.urls import path
from . import views

app_name ='blog'

urlpatterns=[
path('',views.blog,name='blog'),
path('<int:num>/',views.blog_detail,name='post_detail'),
path('category/<str:cat>/',views.blog,name='category'),
path('author/<str:author>/',views.blog,name='author')


]