from django.urls import path
from . import views


urlpatterns = [
    path(r'page/<int:pk>/', views.page, name='page'),
    path(r'post/<int:id>/', views.post, name='post'),
    path(r'category/<str:cate_name>/',
         views.category, name='category'),
    path(r'tag/<int:tag_name>/',
         views.tag, name='tag'),
    path(r'archive/<int:year>/<int:month>/',
         views.archive, name='month'),
    path(r'archive/<int:year>/', views.archive, name='year'),
    path(r'archive/', views.archive, name='all'),
    path(r'friendlink/', views.link, name='friendlink'),
    path(r'', views.index, name='index'),
]
