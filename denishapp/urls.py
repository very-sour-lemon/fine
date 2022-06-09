from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.DenishList.as_view(), name='list'),
    path('create/', views.DenishCreate.as_view(), name='create'),
    path('', views.home, name="home"),
    path('main', views.main, name="main"),
    path('tech/', views.tech, name="tech"),
    path('sci/', views.sci, name="sci"),
    path('use/', views.use, name="use"),
]
