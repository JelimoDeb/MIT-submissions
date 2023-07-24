from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def projects(request):
    return render(request, 'projects.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def blogdetails(request):
    return render(request, 'blog-details.html')

def project(request):
    return render(request, 'project-details.html')

def sample(request):
    return render(request, 'sample-inner-page.html')

def service(request):
    return render(request, 'service-details.html')
