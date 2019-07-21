from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def signup(request):
    # 로그인 후 회원 가입 페이지 막기
    if request.user.is_authenticated:
        return redirect('posts:list')
    # HTTP Method가 POST 인 경우    
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
        # 모델폼의 유효성 검증이 valid할 경우, DB에 저장
        if signup_form.is_valid():
            user = signup_form.save()
            # 회원 가입 후 자동 로그인 코드
            auth_login(request, user)
            return redirect('read')
    
    #HTTP Method가 GET 인 경우
    else:
        signup_form = UserCreationForm()
    
    return render(request, 'accounts/signup.html', {'signup_form':signup_form})

def login(request):
    if request.user.is_authenticated:
        return redirect('read')

    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
        return redirect('read')
    
    else:
        login_form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'login_form' : login_form})

 # def logout(request):
    # auth_logout(request)
    # return redirect('login')

