from django.urls import path
from . import views  # 導入視圖

app_name = "admins"
urlpatterns = [
    # 後台 管理者- 登入 首頁 
    # http://127.0.0.1:8000/admin/
    path('login/', views.login, name='login'),
    path('', views.index, name="index"),

    # 後台 管理者- 登出 註冊 重置密碼 
    # http://127.0.0.1:8000/admin/logout
    path('logout/', views.logout, name="logout"),
    # http://127.0.0.1:8000/admin/signup
    path('signup/', views.signup, name="signup"),
    # http://127.0.0.1:8000/admin/reset
    path('reset/', views.reset, name="reset"),

]