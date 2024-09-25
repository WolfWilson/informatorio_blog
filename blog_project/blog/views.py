from django.shortcuts import render

def index(request):
    return render(request, 'cinema-world/index.html')

def about(request):
    return render(request, 'cinema-world/about-us.html')

def contact(request):
    return render(request, 'cinema-world/contact-us.html')

def articles(request):
    return render(request, 'cinema-world/articles.html')
