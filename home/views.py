from django.shortcuts import render, HttpResponseRedirect, redirect

# Create your views here.


def index(request):
    return page(request, 1)


def page(request, pk):
    pass


def post(requst, id):
    pass


def category(request, cate):
    pass


def tag(request, tag):
    pass


def archive(request, year=None, month=None, day=None):
    pass


def link(request):
    pass
