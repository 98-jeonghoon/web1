from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
# id, account_id, password, email, nickname, name, phone_number
from .models import User

@csrf_exempt
def register(request):
    if request.method == 'GET':
        print(request.GET)
        return render(request, 'signup.html')
    elif request.method == 'POST':
        # print(request.POST)
        if request.POST.get('password1') == request.POST.get('password2'):
            user = User.objects.create_user(
                account_id = request.POST.get('account_id'),
                password = request.POST.get('password1',""),
                name = request.POST.get('name',""),
                email = request.POST.get('email',""),
                nickname = request.POST.get('nickname',""),
                phone_number = request.POST.get('phone_number',""),
            )
            # print(user)
            auth.login(request, user)
            return render(request, 'signup_ok.html', context = {"account_id" : user.account_id})
        
@csrf_exempt
def login(request):
    if request.method == 'POST':
        account_id = request.POST.get('account_id')
        password = request.POST.get('password')
        user = auth.authenticate(request, account_id=account_id, password=password)
        print(request.POST)
        print(user)
        if user is not None:
            auth.login(request, user)
            return render(request, 'Base_page.html')
        else:
            return render(request, 'login.html', {'error : ' '등록되지 않은 아이디이거나, 아이디 또는 비밀번호를 잘못 입력하였습니다. '})
        
    else:
        return render(request, 'login.html')
    
@csrf_exempt
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('main.html')
    return render(request, 'signup.html')

class MainView(TemplateView):
    template_name = "Base_page.html"