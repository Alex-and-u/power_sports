from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.shortcuts import render

# Create your views here.

def home(request):
    html_template = loader.get_template('index.html')
    context = {}
    return HttpResponse(html_template.render(context, request))


def about(request):
    html_template = loader.get_template('about.html')
    context = {}
    return HttpResponse(html_template.render(context, request))


def blog(request):
    html_template = loader.get_template('blog.html')
    context = {}
    return HttpResponse(html_template.render(context, request))


def contact(request):
    html_template = loader.get_template('contact.html')
    context = {}
    return HttpResponse(html_template.render(context, request))


def news(request):
    html_template = loader.get_template('news.html')
    context = {}
    return HttpResponse(html_template.render(context, request))


def single_blog(request):
    html_template = loader.get_template('single-blog.html')
    context = {}
    return HttpResponse(html_template.render(context, request))


def team(request):
    html_template = loader.get_template('team.html')
    context = {}
    return HttpResponse(html_template.render(context, request))