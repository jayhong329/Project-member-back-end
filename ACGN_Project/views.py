from django.shortcuts import render

# 配合urls.py預設路徑''時渲染index.html
# def index(request):
#     return render(request, 'admins/index.html', {"title": "管理者首頁"})


# 回傳所有html檔名以便連結
def render_template(request, template_name):
    return render(request, f'{template_name}.html')
