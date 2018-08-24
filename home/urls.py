from django.urls import path
from . import views


urlpatterns = [
    path(r'page/<int:pk>/', views.page, name='page'),
    path(r'post/<int:id>/', )
    path(r'', views.index, name='index'),
]
