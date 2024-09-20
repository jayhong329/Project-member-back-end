from django.urls import path
from Example_APP import views 

app_name='Example_APP'
# http://127.0.0.1:8000/Example_APP/
urlpatterns = [
    path('', views.index, name='index'),
]
