from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('display/1.html', views.display_article_1, name='display_article_1'),
    path('display/2.html', views.display_article_2, name='display_article_2'),
]

# from django.urls import path
# from .views import index
#
# urlpatterns = [
#     path('', index, name='index'),
#     # path('/display1',name='display1'),
#     # path('/display2',name='display2'),
# ]