from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permission import AllowAny 
from .serializers import UserSerializer
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model 
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout 

# Create your views here.
import random
import re
def generate_session_token(length=10):
    return ''.join(random.SystemRandom.choice([chr(i) for i in range(97,123)]+ [str(i) for i in range(10)]) for _ in range(length))

def signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'Send a post request'})
    
    username = request.POST['email']
    password = request.POST['password']

    if not re.match("^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$",username):
        return JsonResponse({'error': 'Send a valid username/email'})
    
    if len(password) < 3:
        return JsonResponse({'error':'Send a valid password'}) 
    
    UserModel = get_user_model()
    try :
        pass
    except UserModel.DoesNotExist:
        return JsonResponse({'error':'Invalid Email'})