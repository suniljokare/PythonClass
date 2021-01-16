from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.

def Enquiry(request):
    if request.method=='GET':

        form=EnquiryForm()
        return render(request,'enquiry/enquiry.html',{"form":form})
    else:
        print(request.POST,"DATTA")

        form=EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'enquiry/thank_you.html') 