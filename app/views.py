from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from django.views.generic import *
# Create your views here.


class Temp(TemplateView):
    template_name='temp.html'
    def get_context_data(self, **kwargs):
        ECDO=  super().get_context_data(**kwargs)
        ECDO['SFO']=SchoolForm
        return ECDO
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Inserted Data Successfully..')
        
class SchoolInsertForm(FormView):
    form_class=SchoolForm
    template_name='SchoolInsertForm.html'

    def form_valid(self,form):
        form.save()
        return HttpResponse('Data is inserted')

class DisplaySchool(ListView):
    model=School
    template_name='DisplaySchool.html'
    context_object_name='sclist'
    ordering=['Sage']



