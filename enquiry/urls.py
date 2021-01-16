from django.contrib import admin
from django.urls import path
from enquiry.views import *
urlpatterns = [
    path('enquiry/', Enquiry,name="enquiry"),
    

]
