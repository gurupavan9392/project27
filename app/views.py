
from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView
from app.forms import *
from django.http import HttpResponse


class isbyfv(FormView):
    template_name='isbyfv.html'
    form_class=StudentFV

    def form_valid(self,form):
        form.save()
        return HttpResponse('form created')
        