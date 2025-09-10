from django.shortcuts import render
from django.views.generic.list import ListView
from studentorg.models import Organization

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'  # the variable name used in the template for the queryset
    template_name = "home.html"
