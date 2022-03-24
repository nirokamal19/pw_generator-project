from operator import length_hint
from secrets import choice
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):

    thepassword = ''

    characters = list('abcdefghijklmnopqrstuvwxyz')
    upper_list = list('ABCDEFGHIJKLMNOPQRSTUV')
    special_list = list('!@£$%^&*.')
    number_list = list('1234567890')
    length = int(request.GET.get('length', 8))

    for x in range(length):
        thepassword += random.choice(characters)

#Requests for checkboxes
    if request.GET.get('uppercase'):
        if not any(i in thepassword for i in upper_list):
            thepassword = thepassword.replace(random.choice(thepassword), random.choice(upper_list))
        # thepassword = thepassword.replace(random.choice(thepassword), random.choice(upper_list))
        characters.append(random.choice(upper_list))

    if request.GET.get('special'):
        if not any(i in thepassword for i in special_list):
            thepassword = thepassword.replace(random.choice(thepassword), random.choice(special_list))
        characters.extend(list(special_list))

    if request.GET.get('numbers'):
        if not any(i in thepassword for i in number_list):
            thepassword = thepassword.replace(random.choice(thepassword), random.choice(number_list))
        characters.extend(list(number_list))

    return render(request, 'generator/password.html', {'password':thepassword})
