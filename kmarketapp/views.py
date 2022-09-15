from django.shortcuts import redirect, render
from .models import *

default_data = {
    'user_roles': UserRole.objects.all(),
}

def signup_page(request):
    return render(request, "signup_page.html", default_data)

def login_page(request):
    return render(request, "login_page.html", default_data)

def forget_password_page(request):
    return render(request, "forget_password_page.html", default_data)

def profile_page(request):
    return render(request, "profile_page.html", default_data)

# get data from signup page
# signup functionality
def signup(request):
    print(request.POST)

    user_role = UserRole.objects.get(id=int(request.POST['user_role']))

    # ORM - Object Relational Mapping
    master = Master.objects.create(
        UserRole = user_role,
        Email = request.POST['email'],
        Password = request.POST['password'],
    )

    UserProfile.objects.create(
        Master = master,
    )

    return redirect(signup_page)

# login functionality
def login(request):
    master = Master.objects.get(Email = request.POST['email'])
    default_data['master']=master
    return redirect(profile_page)