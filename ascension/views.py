from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, FormView

from .forms import InquiryForm

# Create your views here.
class IndexView(TemplateView):
    template_name = 'ascension/index.html'

class InquiryView(FormView):
    template_name = 'ascension/inquiry.html'
    form_class = InquiryForm
