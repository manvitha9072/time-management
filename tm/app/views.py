from django.shortcuts import redirect, render, HttpResponse
from app.models import Home
from app.models import Newschedule
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == "POST" :
        name=request.POST.get('name')
        phnumber=request.POST.get('phnumber')
        mailid=request.POST.get('mailid')
        prof=request.POST.get('prof')
        age=request.POST.get('age')
        home = Home(name=name, phnumber=phnumber, mailid=mailid, prof=prof, age=age)
        home.save()
    return render(request, "home.html")

def newschedule(request):
    if request.method == "POST" :
        name=request.POST.get('name')
        time=request.POST.get('time')
        title=request.POST.get('title')
        desc=request.POST.get('desc') 
        newschedule = Newschedule(name=name, time=time, title=title, desc=desc)
        newschedule.save()
        return redirect("/")
    return render(request, 'newschedule.html')

def yourschedule(request):
    if request.method == "POST" :
        return HttpResponse("invalid method")
    username = request.POST.get("username")
    print(username)
    password = request.POST.get("password")
    print(password)
    rememberme = request.POST.get("rememberme")
    if not rememberme:
        request.session.set_expiry(0)
    else:
        request.session.set_expiry(86400)
    user = authenticate(username=username, password=password)
    print(user)
    if user is not None:
        login(request, user)
        messages.add_message(request, messages.SUCCESS, 'Login Successfull')
        return redirect("/loginview")
    messages.add_message(request, messages.ERROR, 'Invalid Username or Password')
    return render(request, 'login.html')

def loginview(request):
    if request.user.is_authenticated:
        return render(request, "loginview.html")
    return render(request, "login.html")

def editschedule(request):
    return HttpResponse("edit schedule")

def mentorship(request):
    return HttpResponse("mentorship page")

def recomendation(request):
    return HttpResponse("recomendation page")

def track(request):
    return HttpResponse("track page")
