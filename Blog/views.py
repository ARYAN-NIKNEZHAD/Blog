from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("index")


def post_list(request):
    return HttpResponse("Post list")


def post_detail(request, id):
    return HttpResponse(f"Post{id}")

