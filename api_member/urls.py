from django.urls import path
from . import views

app_name = "api_member"
urlpatterns = [
    # http://127.0.0.1:8000/api_member/
    path('', views.index, name="index"),
    # http://127.0.0.1:8000/api_member/register
    path('register/', views.register),
    # http://127.0.0.1:8000/api_member/checkname/
    path('checkname/', views.checkname ),
    # http://127.0.0.1:8000/api_member/checkphone/
    path('checkphone/', views.checkphone ),
    # http://127.0.0.1:8000/api_member/checkemail/
    path('checkemail/', views.checkemail ),
    # http://127.0.0.1:8000/api_member/checkpassword/
    path('checkpassword/', views.checkpassword ),
    # http://127.0.0.1:8000/api_member/search/
    path('search/', views.search, name="search" ),
    # http://127.0.0.1:8000/api_member/signup
    path('signup/', views.signup, name='signup'),
        # http://127.0.0.1:8000/api_member/personal/
    path('personal/', views.personal ),
    # http://127.0.0.1:8000/api_member/privacy_setting/
    path('privacy_setting/', views.privacy_setting, name="privacy_setting" ),


    # http://127.0.0.1:8000/api_member/send_reset_email/
    path('send_reset_email/', views.send_reset_email, name='send_reset_email'),
    # http://127.0.0.1:8000/api_member/request-verification/
    path('request-verification/', views.request_verification, name='request_verification'),
    # http://127.0.0.1:8000/api_member/send_verification_email/
    path('send_verification_email/', views.send_verification_email, name='send_verification_email'),
    # http://127.0.0.1:8000/api_member/verify_code/
    path('verify_code/', views.verify_code, name='verify_code'),
    # http://127.0.0.1:8000/api_member/reset_confirm
    path('reset_confirm/', views.reset_confirm, name='reset_confirm'),
    # http://127.0.0.1:8000/api_member/email_change/
    path('email_change/', views.email_change, name='email_change'),
    # http://127.0.0.1:8000/api_member/email_change_confirm/
    path('email_change_confirm/<str:token>/', views.email_change_confirm, name='email_change_confirm'),
    # http://127.0.0.1:8000/api_member/verify-email/
    path('verify-email/<str:token>/', views.verify_email, name='verify_email'),

    
    # http://127.0.0.1:8000/api_member/reset_email/
    path('reset_email/', views.reset_email, name='reset_email'),
    # http://127.0.0.1:8000/api_member/reconfirm_email/<str:token>/
    path('reconfirm_email/<str:token>/', views.reconfirm_email, name='reconfirm_email'),
    # http://127.0.0.1:8000/api_member/reset_phone/
    path('reset_phone/', views.reset_phone, name='reset_phone'),
    # http://127.0.0.1:8000/api_member/reconfirm_phone/<str:token>/
    path('reconfirm_phone/<str:token>/', views.reconfirm_phone, name='reconfirm_phone'),



    # http://127.0.0.1:8000/api_member/phone_change/
    path('phone_change/', views.phone_change, name='phone_change'),
    # http://127.0.0.1:8000/api_member/phone_change_confirm/<str:token>/
    path('phone_change_confirm/<str:token>/', views.phone_change_confirm, name='phone_change_confirm'),

]