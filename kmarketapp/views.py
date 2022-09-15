from django.shortcuts import render

default_data ={}

def signup_page(request):
    return render(request,"signup_page.html",default_data)
    