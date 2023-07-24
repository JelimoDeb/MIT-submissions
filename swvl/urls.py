from django.urls import path
from . import views

app_name = "swvl"  # maintain this.
urlpatterns = [

    path('',views.home, name="index"),
    path('about/',views.about, name="about"),
    path('services/',views.services, name="services"),
    path('projects/',views.projects, name="projects"),
    path('blog/',views.blog, name="blog"),
    path('blogdetails/',views.blogdetails, name="blog-details"),
    path('project/',views.project, name="project-details"),
    path('sample/',views.sample, name="sample-inner-page"),
    path('service/',views.service, name="service-details"),


]