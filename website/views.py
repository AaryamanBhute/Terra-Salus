from django.shortcuts import render

# Create your views here.
def home(request):
    return(render(request, "website/main.html"))
def about(request):
    return(render(request, "website/about.html"))
def contact(request):
    return(render(request, "website/contact.html"))
def leadership(request):
    return(render(request, "website/leadership.html"))
def join(request):
    return(render(request, "website/join.html"))