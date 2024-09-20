from django.contrib import admin
from django.urls import path, include # 導入個人應用程式
from django.conf import settings
from django.conf.urls.static import static

from . import views  # 導入專案的 views.py(自己手動建的)

urlpatterns = [
    path('admin/', admin.site.urls),

    
    # 預設路徑(http://127.0.0.1:8000/)時
    # 去找專案資料夾下的views.py(自己手動建的)的 index 函數
    path('', views.index, name='index'),


    # http://127.0.0.1:8000/<str:template_name>.html 
    # 以確保操作index時其餘頁面都能正常連結到
    path('<str:template_name>.html', views.render_template, name='render_template'),
    

    # http://127.0.0.1:8000/Example_APP/ 
    # 假設我們各自導入自己的應用程式(Example_APP)個人操作的模樣
    path('Example_APP/', include('Example_APP.urls')),
    # member-app
    # http://127.0.0.1:8000/member/ 
    path('member/', include('member.urls')),
    # http://127.0.0.1:8000/api_member/ 
    path('api_member/', include('api_member.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
