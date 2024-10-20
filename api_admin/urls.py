from django.urls import path
from . import views  # 導入視圖

app_name = "api_admin"
urlpatterns = [
    # http://127.0.0.1:8000/api_admin/signup
    path('signup/', views.signup, name="signup"),
    # http://127.0.0.1:8000/api_admin/reset
    path('reset/', views.reset, name="reset"),

]