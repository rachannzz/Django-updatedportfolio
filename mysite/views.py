from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"mysite/base.html")


def about(request):
    return render (request,"mysite/about.html")


def skills(request):
    return render (request,"mysite/skills.html")


def Teams(request):
    return render (request,"mysite/Teams.html")


def contact(request):
    return render (request,"mysite/contact.html")