from django.contrib import admin
from django.urls import path
from .views import signupview,loginview,listview,detailview,CreateClass,logoutview,evaluationview
from django.contrib.auth import views as auth_views
from .views import emailfunc

urlpatterns=[
    path('email/',emailfunc),
    path('signup/',signupview,name='signup'),
    path('login/',loginview,name='login'),
    path('list/',listview,name='list'),
    path('detail/<int:pk>/',detailview,name='detail'),
    path('create/',CreateClass.as_view(),name='create'),
    path('logout/',logoutview,name='logout'),
    path('evaluation/<int:pk>',evaluationview,name='evaluation'),
    path('change-password/',
    auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'),
    ),
]
