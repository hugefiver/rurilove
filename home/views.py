from django.shortcuts import (render, HttpResponseRedirect,
                              redirect, get_object_or_404)
from django.db import models
from .models import *
import random
import markdown

# Create your views here.
post_per_page = 10


def index(request):
    return page(request, 1)


def page(request, pk):
    posts = Post.objects.filter(draft=False)
    count = posts.count()
    end = post_per_page * abs(pk)
    start = end - post_per_page
    if pk and count and count > start:
        post_list = posts[start:end]
        context = {'post_list': post_list,
                   'page': pk,
                   'pages': range(1, (count-1)//post_per_page+2)}
        if pk < count//post_per_page - 1:
            context['next_page'] = pk+1
        if pk > 1:
            context['pre_page'] = pk-1
    else:
        context = {'post_list': None,
                   'pages': range(1, (count-1)//post_per_page+2) if count>0 else [1]}
    return render(request, 'home/page.html', context)


def post(request, id):
    p = get_object_or_404(Post, id=id, draft=False)
    p.view_count += 1
    p.save()

    md_extensions = ['markdown.extensions.extra',
                     'markdown.extensions.fenced_code',
                     'markdown.extensions.codehilite']
    if p.toc:
        md_extensions.append('markdown.extensions.toc')
    p.body = markdown.markdown(p.body, extensions=md_extensions)

    if p.has_music:
        if not p.music:
            m = Music.objects
            p.music = m.all()[random.randrange(m.count())]

    comments = p.comment_set.all()
    comment_list = []
    for comment in comments:
        comment.body = markdown.markdown(comment.body)
        comment_list.append(comment)

    context = {'post': post,
               'comment_list': comment_list}
    if Post.objects.filter(id=pk+1, draft=False):
        context['next_post'] = Post.objects.get(id=pk+1, draft=False)
    if Post.objects.filter(id=pk-1, draft=False):
        context['pre'] = Post.objects.get(id=pk-1, draft=False)
    return render(request, 'home/post.html', context)


def category(request, cate_name):
    post_list = Post.objects.filter(catt=cate_name, draft=False)
    category_list = Category.objects.annotate(count=models.Count('post')).filter(count__gt=0)
    return render(request, 'home/tag.html',
                  context={'post_list': post_list,
                           'category': cate_name,
                           'category_list': category_list})


def tag(request, tag_name):
    post_list = Post.objects.filter(tag=tag_name, draft=False)
    tag_list = Tag.objects.annotate(count=models.Count('post')).filter(count__gt=0)
    return render(request, 'home/tag.html',
                  context={'post_list': post_list,
                           'tag': tag_name,
                           'tag_list': tag_list})


def archive(request, year=None, month=None):
    post_list = Post.objects.all()
    time = []
    if year:
        post_list = post_list.filter(create_time__year=year)
        time.append(year+'年')
        if month:
            post_list = post_list.filter(create_time__month=month)
            time.append(month+'月')
    context = {'post_list': post_list,
               'date': ''.join(time) if time else '全部文章'}
    return render(request, 'home/tag.html', context)


def author(request, author):
    pass


def link(request):
    links = FriendLink.objects.all()
    return render(request, 'home/link.html', context={'link_list': links})
