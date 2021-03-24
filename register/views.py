import os
import json
import numpy as np
from django.shortcuts import render, HttpResponse, redirect
# from register.models import SignUp, Face
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from .forms import SignupForm, FaceForm
from register.models import UserProfile
from .face import get_FE, face_detect

def index(request):
    return render(request, 'index.html')
    
def sign_up(request):
    if request.method == "POST":
        username = request.POST.get('username')
        # username = request.POST.get('email')
        password1 = request.POST.get('psw')
        password2 = request.POST.get('psw-repeat')

        if(password1 != password2):
            messages.error(request, 'Passwords dont match!', extra_tags='danger')
            return render(request, 'sign_up.html')

        face_input = request.POST.get('input_face')
        isFace, encoding = get_FE(face_input)
        if(isFace):
            encoding = json.dumps(encoding.tolist())
            user = User.objects.create_user(username = username, password = password1)
            UserProfile.objects.create(user = user, face_data = encoding)
            messages.success(request, 'Profile created succesfully!')
            return redirect("/login")
        
        else:
            messages.error(request, 'No faces detected. Try again.', extra_tags='danger')
        
        # messages.success(request, 'Signup succesful!')
    
    return render(request, 'sign_up.html')


def loginUser(request):
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('psw')
        face_input = request.POST.get('input_face')

        valid = False

        if password:
            user = authenticate(username = username, password = password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect("welcome")
            else:
                messages.error(request, 'Invalid Credentials. Try again.', extra_tags='danger')
                return render(request, 'login.html')

        else:
            userQuery = User.objects.filter(username=username)
            if userQuery.exists():
                user = userQuery[0]
                valid = True
        
        if valid:
            gold_face = np.array(json.loads(user.user_profile.face_data))
            isFace, check_face = get_FE(face_input)

            if(isFace and face_detect(gold_face, check_face)):
                login(request, user)
                return redirect("welcome")
            else:
                messages.error(request, 'Faces do not match!', extra_tags='danger')

        else:
            messages.error(request, 'No User Found! Try Again', extra_tags='danger')
    return render(request, 'login.html')

def welcome(request):
    if request.user.is_anonymous:
        messages.error(request, 'Please login first', extra_tags='danger')
        return redirect("login")
    return render(request, 'welcome.html')


def logoutUser(request):
    logout(request)
    return redirect("login")



# def sign_up(request):
#     if request.method == "POST":
#         form = SignupForm(request.POST)
#         face_form = FaceForm(request.POST)
#         print(face_form)
#         if(form.is_valid() and face_form.is_valid()):
#             # form.save()
#             # messages.success(request, 'Signup succesful!')
#             user = form.save()
#             face = face_form.save(commit=False)
#             face.user = user
#             face.save()
#             return redirect("login")
#         else:
#             for msg in form.error_messages:
#                 print(form.error_messages[msg])

#             return render(request, 'sign_up.html', {'form' : form})
    
#     form = SignupForm()
#     face_form = FaceForm(request.POST)
#     return render(request, 'sign_up.html', {'form' : form, 'face_form' : face_form})