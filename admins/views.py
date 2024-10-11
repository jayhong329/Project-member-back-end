from django.shortcuts import render, redirect
from django.http import JsonResponse
from api_member.models import AuthUser
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
from django.contrib import messages
from django.core.cache import cache
import json

# Create your views here.
# 後台 管理頁面 "登入 首頁 登出"
def login(request):
    return render(request, 'admins/login.html', {"title": "管理者登入"})

# 後台-管理者 登出 OK 但sesion沒清除 x
def logout(request):
    return render(request, 'admins/login.html', {"title": "管理者登出"})

# 後台-管理者登入後的頁面
def index(request):
    return render(request, 'admins/index.html', {"title": "管理者主頁"})

# 後台-管理者 "註冊"並存入資料庫
def signup(request):
    return render(request, 'admins/signup.html', {"title": "管理者註冊頁面"})

# 後台-管理者 "重置密碼"並更新於資料庫
def reset(request):
    return render(request, 'admins/reset.html', {"title": "管理者重置密碼"})