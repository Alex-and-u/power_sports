from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .forms import RegisterForm, LoginForm, ChoiceForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import JoinEvent
from .models import Booking


def home(request):
    html_template = loader.get_template('index.html')
    context = {}
    return HttpResponse(html_template.render(context, request))


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
    return render(request, 'login.html', {'form': form, "msg": msg})


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'reset_password.html'
    email_template_name = 'reset_password_sent.html'
    confirm_template_name = 'reset.html'
    complete_template_name = 'reset_password_complete.html'
    success_url = reverse_lazy('login')


def user_logout(request):
    logout(request)
    return redirect('login')


def about(request):
    html_template = loader.get_template('about.html')
    context = {}
    return HttpResponse(html_template.render(context, request))


def join(request):
    form = JoinEvent(request.POST or None)
    html_template = loader.get_template('join.html')
    if request.method == request.GET:
        if form.is_valid():
            return render(request, 'events.html')
    else:
        form = JoinEvent()
    context = {'form': form}
    return HttpResponse(html_template.render(context, request))


def events(request):
    event_list = Booking.objects.all()
    # html_template = loader.get_template('events.html')
    # context = {'event_list': event_list}
    return render(request, 'events.html', {'event_list': event_list})


def contact(request):
    html_template = loader.get_template('contact.html')
    context = {}
    return HttpResponse(html_template.render(context, request))


def sports(request):
    form = ChoiceForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'sports.html', context)


def tennis(request):
    form = ChoiceForm(request.POST or None)
    html_template = loader.get_template('Tennis.html')
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/join')
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
            return HttpResponseRedirect('/join')
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
            return HttpResponseRedirect('/join')

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
            return HttpResponseRedirect('/join')
    else:
        form = ChoiceForm()
    context = {'form': form}
    return HttpResponse(html_template.render(context, request))
