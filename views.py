
from django.shortcuts import render

def  home(request):
    return render(request,"index.html")

def contact(request):
    return render(request,"contact.html")
def about(request):
    return render(request, "about.html")
def blog(request):
    return render(request,"blog.html")

def team(request):
    return render(request, "team.html")
def gallery(request):
    return render(request, "gallary.html")
def services(request):
    return render(request, "services.html")
def features(request):
    return render(request, "feature.html")
def FAQs(request):
    return render(request,"FAQs.html")