from django.shortcuts import redirect, render
from .models import *

default_data = {
    'user_roles': UserRole.objects.all(),
}

def signup_page(request):
    return render(request, "signup_page.html", default_data)

def login_page(request):
    if 'email' in request.session:
        return redirect(profile_page)
        
    return render(request, "login_page.html", default_data)

def forget_password_page(request):
    return render(request, "forget_password_page.html", default_data)

def profile_page(request):
    if 'email' not in request.session:
        return redirect(login_page)
    profile_data(request) # call profile data
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

# profile data
def profile_data(request):
    master = Master.objects.get(Email = request.session['email'])
    profile = UserProfile.objects.get(Master = master)

    default_data['profile_data'] = profile

# profile update functionality
def profile_update(request):
    master = Master.objects.get(Email = request.session['email'])
    profile = UserProfile.objects.get(Master = master)

    profile.FullName = request.POST['full_name']
    profile.Gender = request.POST['gender']
    profile.Mobile = request.POST['mobile']
    profile.BirthDate = request.POST['birth_date']
    profile.Country = request.POST['country']
    profile.State = request.POST['state']
    profile.City = request.POST['city']
    profile.Address = request.POST['address']

    profile.save()

    print('profile updated successfully.')

    return redirect(profile_page)

# login functionality
def login(request):
    try:
        master = Master.objects.get(Email = request.POST['email'])
        if master.Password == request.POST['password']:
            request.session['email'] = master.Email
            
            return redirect(profile_page)
        else:
            print('incorrect password')

    except Master.DoesNotExist as err:
        print('something went wrong', err)
    
    return redirect(login_page)

# logout 
def logout(request):
    if 'email' in request.session:
        del request.session['email']
    
    return redirect(login_page)