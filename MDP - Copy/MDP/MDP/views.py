from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import pickle
import numpy as np
from apps.models import Feedback


@login_required
def HomePage(request):
    return render(request, 'home.html', {})


def Register(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        new_user = User.objects.create_user(name, email, password)
        new_user.save()
        return redirect('login')

    return render(request, 'register.html', {})


def Login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Error, user does not exist')

    return render(request, 'login.html', {})


def logoutuser(request):
    logout(request)
    return redirect('login')




# Load the saved model
RF_pkl_filename = 'RandomForest.pkl'  # Replace with the path to your .pkl file
with open(RF_pkl_filename, 'rb') as Model_pkl:
    loaded_model = pickle.load(Model_pkl)

def predict(request):
    result = None

    if request.method == 'POST':
        # Retrieve user input from the frontend form
        Vegetable =request.POST['Vegetable']
        if Vegetable == "potato":
            Vegetable=13
        elif Vegetable == "tomato":
            Vegetable=16
        elif Vegetable == "peas":
            Vegetable=11
        elif Vegetable == "pumpkin":
            Vegetable=14
        elif Vegetable == "cucmber":
            Vegetable=6
        elif Vegetable == "pointed grourd":
            Vegetable=12
        elif Vegetable == "raddish":
            Vegetable=1
        elif Vegetable == "bitter gourd":
            Vegetable=0
        elif Vegetable == "onion":
            Vegetable=10
        elif Vegetable == "garlic":
            Vegetable=7
        elif Vegetable == "cabage":
            Vegetable=3
        elif Vegetable == "califlower":
            Vegetable=4
        elif Vegetable == "chilly":
            Vegetable=5
        elif Vegetable == "okra":
            Vegetable=9
        elif Vegetable == "brinjal":
            Vegetable=2
        elif Vegetable == "ginger":
            Vegetable=8
        elif Vegetable == "radish":
            Vegetable=15
        season = request.POST['season']
        if season=="winter":
            season=4
        elif season=="summer":
            season=3
        elif season=="spring":
            season=2
        elif season=="monsoon":
            season=1
        elif season=="autumn":
            season=0
        month = request.POST['Month']
        if month=="jan":
            month=4
        elif month=="apr":
            month=1
        elif month=="july":
            month=5
        elif month=="sept":
            month=10
        elif month=="oct":
            month=3
        elif month=="dec":
            month=3
        elif month=="may":
            month=8
        elif month=="aug":
            month=2
        elif month=="june":
            month=7
        elif month=="march":
            month=7
        elif month=="dont know":
            month=0
        Temperature = request.POST['Temperature']
        Disaster_happend = request.POST['Disaster_happend']
        if Disaster_happend=="yes":
            Disaster_happend=1
        elif Disaster_happend=="no":
            Disaster_happend=0
        Vegetable_condition = request.POST['Vegetable_condition']
        if Vegetable_condition=="fresh":
             Vegetable_condition=1
        elif Vegetable_condition=="scrap":
             Vegetable_condition=3
        elif Vegetable_condition=="average":
             Vegetable_condition=0
        elif Vegetable_condition=="scarp":
             Vegetable_condition=2
        # Add more fields as needed

        # Prepare the input data for prediction
        input_data = [Vegetable, season, month,Temperature, Disaster_happend, Vegetable_condition]  # Adjust this according to your model's input features
        input_data_as_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_array.reshape(1, -1)

        # Make prediction using the loaded model
        prediction = loaded_model.predict(input_data_reshaped)
        print("The predicted value is",prediction)
        # Display prediction result

    return render(request, 'home.html', {'result': prediction})



def feedback(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        feedback = request.POST['feedback']
        ins = Feedback(name=name, email=email, phonenumber=phonenumber, feedback=feedback)
        ins.save()
        print("ok")
    return render(request, 'feedback.html', {})


def contact(request):
    return render(request, 'contact.html',{})


def precautions(request):
    return render(request, 'about.html',{})