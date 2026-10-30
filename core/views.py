from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def contact_view(request):
    return render(request, 'contact.html')

def projects_view(request):
    return render(request, 'projects.html')

def services_view(request):
    return render(request, 'services.html')

def about_view(request):
    return render(request, 'about.html')