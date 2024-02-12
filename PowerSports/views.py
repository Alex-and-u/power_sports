from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .forms import RegisterForm, LoginForm, FieldForm, ChoiceForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def home(request):
    html_template = loader.get_template('index.html')
    context = {}
    return HttpResponse(html_template.render(context, request))

# def register(request):
#     html_template = loader.get_template('register.html')
#     context = {}
#     return HttpResponseRedirect(html_template.render(context, request))

def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            msg = 'Invalid credentials'
    else:
        msg = "Invalid user data"
    return render(request, 'login.html', {'form': form, "msg":msg})



def user_logout(request):
    logout(request)
    return redirect('login')


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
    form = ChoiceForm()
    html_template = loader.get_template('news.html')
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request,'news.html', context)


def single_blog(request):
    html_template = loader.get_template('single-blog.html')
    context = {}
    return HttpResponse(html_template.render(context, request))


def tennis(request):
    form = ChoiceForm(request.POST or None)
    html_template = loader.get_template('Tennis.html')
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    else:
        form = ChoiceForm()
    context = {'form': form}
    return HttpResponse(html_template.render(context, request))

def footbal(request):
    form = ChoiceForm(request.POST or None)
    html_template = loader.get_template('Football.html')
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    else:
        form = ChoiceForm()
    context = {'form': form}
    return HttpResponse(html_template.render(context, request))

def voleyball(request):
    form = ChoiceForm(request.POST or None)
    html_template = loader.get_template('Voleyball.html')
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    else:
        form = ChoiceForm()
    context = {'form': form}
    return HttpResponse(html_template.render(context, request))

def basketball(request):
    form = ChoiceForm(request.POST or None)
    html_template = loader.get_template('Basketball.html')
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    else:
        form = ChoiceForm()
    context = {'form': form}
    return HttpResponse(html_template.render(context, request))




