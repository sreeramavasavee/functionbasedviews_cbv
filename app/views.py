from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *
# Create your views here.
#function basedd viewss
def fbv(request):
    return HttpResponse('this is function based views')

#class based views returning string as a response
class cbv(View):
    def get(self,request):
        return HttpResponse(' this is classbasedview ')
    
#fb templates
def fbv_temp(request):
    return render(request,'fbv_temp.html')

# class based views using template views
class cbv_string(View):
    def get(self,request):
        return render(request,'cbv_string.html')
    
#function based views
def fbv_form(request):
    s=studentform()
    d={'s':s}
    if request.method=='POST':
        sf=studentform(request.POST)
        if sf.is_valid():
            sf.save()
            return HttpResponse('inserted data')
        
    return render(request,'fbv_form.html',d)

#class views inserting data
class cbv_form(View):
    def get(self,request):
        s=studentform()
        d={'s':s}
        return render(request,'cbv_form.html',d)
    
    def post(self,request):
        sf=studentform(request.POST)
        if sf.is_valid():
            sf.save()
            return HttpResponse('inserted data')