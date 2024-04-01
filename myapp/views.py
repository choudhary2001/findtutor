from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib import messages

# Create your views here.
def index(request):
    latest_teachers = Teachers.objects.all().order_by('-date_joined')[:6]
    context = {'latest_teachers': latest_teachers}
    return render(request,'myapp/index.html', context=context)

def become_teacher(request):
    if request.method=="POST":
        print('this is post request ')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        qualification = request.POST.get('qualification')
        experience = request.POST.get('experience')
        subjects_taught = request.POST.get('subjects_taught')
        profile_img = request.FILES.get('profile_image')
        print(first_name, last_name, email, password, phone, address, qualification, profile_img)
        hashed_password = make_password(password)
        user = User(first_name = first_name, last_name = last_name, username=email, email=email, password=hashed_password, is_staff= True)
        user.save()
        teacher = Teachers.objects.create(
            user=user,
            phone_number=phone,
            date_of_birth=dob,
            address=address,
            city=city,
            state=state,
            country=country,
            qualification=qualification,
            experience=experience,
            subjects_taught=subjects_taught,
            profile_img=profile_img
        )
        teacher.save()
        print(teacher)
        messages.success(request, 'You are registered successfully.')
    return render (request,'myapp/signup.html')

def become_student(request):
    if request.method=="POST":
        print('this is post request ')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
     
        hashed_password = make_password(password)
        user = User(first_name = first_name, last_name = last_name, username=email, email=email, password=hashed_password, is_staff= False)
        user.save()
        s = Student.objects.create(
            user=user,
            phone_number=phone,
        )
        s.save()
        print(s)
        messages.success(request, 'You are registered successfully.')
    return render (request,'myapp/studentsignup.html')


def signin(request):
    if request.method == 'POST':
        # Extract username and password from the form submission
        username = request.POST.get('email')
        password = request.POST.get('password')
        print("Email:", username)
        # print("Phone:", phone)
        print("Password:", password)
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # If user is authenticated, log the user in
            login(request, user)
            # Redirect to a success page or any desired page
            return redirect('index')  # Replace 'success_page_url' with the desired URL
        else:
            # If authentication fails, render the login form with an error message
            error_message = "Invalid username or password."
            return render(request, 'myapp/signin.html', {'error_message': error_message})
       
    return render (request,'myapp/signin.html')


def teachers(request):
    subject = request.POST.get('subject', '')
    location = request.POST.get('location', '')

    if subject != '' and location != '':
        latest_teachers = Teachers.objects.filter(subjects_taught__icontains=subject, city__icontains=location).order_by('-date_joined')
    elif subject != '':
        latest_teachers = Teachers.objects.filter(subjects_taught__icontains=subject).order_by('-date_joined')
    elif location != '':
        latest_teachers = Teachers.objects.filter(city__icontains=location).order_by('-date_joined')
    else:
        latest_teachers = Teachers.objects.all().order_by('-date_joined')

    context = {'latest_teachers': latest_teachers}
    return render(request, 'myapp/teachers.html', context=context)


def signout(request):
    logout(request)
    return redirect('index')