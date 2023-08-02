from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app.forms import*
from app.models import*

# Create your views here.
#FBV is returning string as a response

def Fbvstring(request):
    return HttpResponse('<h1> This is FBV of string')


#FBV is returning html page as a response
def Fbvhtml(request):
    return render(request,'Fbvhtml.html')


class Cbvhtml(View):
    def get(self,request):
        return render(request,'Cbvhtml.html')


class Cbvstring(View):
    def get(self,request):
        return HttpResponse('<h1> This is CBV string response</h1>')


class insert_cbv(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'insert_cbv.html',d)

    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('<h1> data is inserted</h1>')
        