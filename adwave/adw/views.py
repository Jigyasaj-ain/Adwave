from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model, authenticate, login as auth_login
from .models import Ad

# Home and other page views
def index(request):
    return render(request, 'adw/index.html')

def about(request):
    return render(request, 'adw/about.html')

def display(request):
    return render(request, 'adw/display.html')

def features(request):
    return render(request, 'adw/features.html')

def feedback(request):
    return render(request, 'adw/feedback.html')

def submitads(request):
    return render(request, 'adw/submitads.html')

# Signup/Login Page View (GET and POST)
def signuplogin(request):
    if request.method == 'POST':
        # Get the form data from the request
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        # Check if passwords match
        if password != password_confirm:
            return render(request, 'adw/signuplogin.html', {'error': 'Passwords do not match.'})

        # Check if user already exists
        if get_user_model().objects.filter(email=email).exists():
            return render(request, 'adw/signuplogin.html', {'error': 'Email is already taken.'})

        if get_user_model().objects.filter(username=username).exists():
            return render(request, 'adw/signuplogin.html', {'error': 'Username is already taken.'})

        # Create the new user
        user = get_user_model().objects.create_user(username=username, email=email, password=password)

        # Redirect to the login page after successful signup
        return redirect('login')

    return render(request, 'adw/signuplogin.html')

# Login view with POST request handling
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            auth_login(request, user)
            return redirect('index')  # Redirect to the home page after login
        else:
            return render(request, 'adw/login.html', {'error': 'Invalid credentials'})

    return render(request, 'adw/login.html')

# Ad submission view
def submit_ad(request):
    if request.method == 'POST':
        adtitle = request.POST.get('adtitle')
        addescription = request.POST.get('addescription')
        adimage = request.FILES.get('adimage')

        # Create and save a new Ad instance
        ad = Ad(adtitle=adtitle, addescription=addescription, adimage=adimage)
        ad.save()

        return HttpResponse("Ad submitted successfully.")

    return render(request, 'adw/submitads.html')
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib.auth import get_user_model, authenticate, login as auth_login
# from .models import Ad

# # Home and other page views
# def index(request):
#     return render(request, 'adw/index.html')

# def about(request):
#     return render(request, 'adw/about.html')

# def display(request):
#     return render(request, 'adw/display.html')

# def features(request):
#     return render(request, 'adw/features.html')

# def feedback(request):
#     return render(request, 'adw/feedback.html')

# def submitads(request):
#     return render(request, 'adw/submitads.html')

# # Sign-up View (Separate from login)
# def signup(request):
#     if request.method == 'POST':
#         # Get the form data from the request
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         password_confirm = request.POST.get('password_confirm')

#         # Check if passwords match
#         if password != password_confirm:
#             return render(request, 'adw/signup.html', {'error': 'Passwords do not match.'})

#         # Check if email or username already exists
#         if get_user_model().objects.filter(email=email).exists():
#             return render(request, 'adw/signup.html', {'error': 'Email is already taken.'})
        
#         if get_user_model().objects.filter(username=username).exists():
#             return render(request, 'adw/signup.html', {'error': 'Username is already taken.'})

#         # Create the new user
#         user = get_user_model().objects.create_user(username=username, email=email, password=password)
        
#         # Log the user in immediately after sign up
#         auth_login(request, user)

#         return redirect('index')  # Redirect to home after signup

#     return render(request, 'adw/signup.html')

# # Login view with POST request handling
# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         # Authenticate the user (by email)
#         try:
#             user = get_user_model().objects.get(email=email)
#         except get_user_model().DoesNotExist:
#             return render(request, 'adw/login.html', {'error': 'Invalid email or password.'})

#         # Verify password
#         if user.check_password(password):
#             auth_login(request, user)
#             return redirect('index')  # Redirect to home page after login
#         else:
#             return render(request, 'adw/login.html', {'error': 'Invalid credentials'})

#     return render(request, 'adw/login.html')

# # Ad submission view
# def submit_ad(request):
#     if request.method == 'POST' and request.FILES.get('adimage'):
#         adtitle = request.POST.get('adtitle')
#         addescription = request.POST.get('addescription')
#         adimage = request.FILES.get('adimage')

#         # Create and save a new Ad instance
#         ad = Ad(adtitle=adtitle, addescription=addescription, adimage=adimage)
#         ad.save()

#         return HttpResponse("Ad submitted successfully.")

#     return render(request, 'adw/submitads.html')
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .models import Ad
# from django.contrib.auth import authenticate, login as auth_login
# from django.shortcuts import render, redirect
# # Home and other page views
# def index(request):
#     return render(request, 'adw/index.html')

# def about(request):
#     return render(request, 'adw/about.html')

# def display(request):
#     return render(request, 'adw/display.html')

# def features(request):
#     return render(request, 'adw/features.html')

# def feedback(request):
#     return render(request, 'adw/feedback.html')

# def submitads(request):
#     return render(request, 'adw/submitads.html')

# # views.py

# from django.shortcuts import render, redirect
# from django.contrib.auth import get_user_model
# from django.contrib.auth import login as auth_login

# from django.shortcuts import render, redirect
# from django.contrib.auth import get_user_model
# from django.http import HttpResponse

# # Signup/Login Page View (GET and POST)
# def signuplogin(request):
#     if request.method == 'POST':
#         # Get the form data from the request
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         password_confirm = request.POST.get('password_confirm')

#         # Check if passwords match
#         if password != password_confirm:
#             return render(request, 'adw/signuplogin.html', {'error': 'Passwords do not match.'})

#         # Check if user already exists
#         if get_user_model().objects.filter(email=email).exists():
#             return render(request, 'adw/signuplogin.html', {'error': 'Email is already taken.'})

#         if get_user_model().objects.filter(username=username).exists():
#             return render(request, 'adw/signuplogin.html', {'error': 'Username is already taken.'})

#         # Create the new user
#         user = get_user_model().objects.create_user(username=username, email=email, password=password)

#         # Redirect to the login page after successful signup
#         return redirect('login')  # Use the name of the login URL pattern

#     return render(request, 'adw/signuplogin.html')

# # Signup/Login Page View (GET and POST)
# # def signuplogin(request):
# #     if request.method == 'POST':
# #         # Get the form data from the request
# #         username = request.POST.get('username')
# #         email = request.POST.get('email')
# #         password = request.POST.get('password')
# #         password_confirm = request.POST.get('password_confirm')

# #         # Check if passwords match
# #         if password != password_confirm:
# #             return render(request, 'adw/signuplogin.html', {'error': 'Passwords do not match.'})

# #         # Check if user already exists
# #         if get_user_model().objects.filter(email=email).exists():
# #             return render(request, 'adw/signuplogin.html', {'error': 'Email is already taken.'})

# #         if get_user_model().objects.filter(username=username).exists():
# #             return render(request, 'adw/signuplogin.html', {'error': 'Username is already taken.'})

# #         # Create the new user
# #         user = get_user_model().objects.create_user(username=username, email=email, password=password)

# #         # Log the user in immediately after signup
# #         auth_login(request, user)

# #         # Redirect to the home page after successful signup and login
# #         return redirect('index')

# #     return render(request, 'adw/signuplogin.html')

# # Login view with POST request handling
# # def login(request):
# #     if request.method == 'POST':
# #         email = request.POST.get('email')
# #         password = request.POST.get('password')

# #         # Authenticate the user
# #         user = authenticate(request, email=email, password=password)

# #         if user is not None:
# #             # Log the user in
# #             auth_login(request, user)
# #             return redirect('index')  # Redirect to the home page after login
# #         else:
# #             return render(request, 'adw/login.html', {'error': 'Invalid credentials'})

# #     return render(request, 'adw/login.html')


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         passwd = request.POST.get('password')

#         # Authenticate the user with username and password
#         user = authenticate(request, username=username, password=passwd)

#         if user is not None:
#             # Log the user in
#             auth_login(request, user)
#             return redirect('index')  # Redirect to the home page after login
#         else:
#             return render(request, 'adw/login.html', {'error': 'Invalid credentials'})

#     return render(request, 'adw/login.html')

# # Ad submission view
# def submit_ad(request):
#     if request.method == 'POST':
#         adtitle = request.POST.get('adtitle')
#         addescription = request.POST.get('addescription')
#         adimage = request.FILES.get('adimage')

#         # Create and save a new Ad instance
#         ad = Ad(adtitle=adtitle, addescription=addescription, adimage=adimage)
#         ad.save()

#         return HttpResponse("Ad submitted successfully.")

#     return render(request, 'adw/submitads.html')
