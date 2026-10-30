from django.contrib import admin
from django.urls import path
from core.views import index_view, contact_view, projects_view, services_view, about_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='home'),                # Paj akey la (http://127.0.0.1:8000/)
    path('contact/', contact_view, name='contact'),  # Paj kontak la
    path('projects/', projects_view, name='projects'),# Paj pwojè yo
    path('services/', services_view, name='services'),# Paj sèvis yo
    path('about/', about_view, name='about'),        # Paj apwopo a
]