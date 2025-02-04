from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'ascension/index.html'
