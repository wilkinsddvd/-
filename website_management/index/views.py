from django.shortcuts import render

# 首页视图
def index(request):
    return render(request, 'index/index.html')

# 显示文章1的视图
def display_article_1(request):
    return render(request, 'display/1.html')

# 显示文章2的视图
def display_article_2(request):
    return render(request, 'display/2.html')

# from django.shortcuts import render
#
# def index(request):
#     return render(request, 'index/index.html')
#
# def login_page(request):
#     return render(request, 'user/login.html')
#
