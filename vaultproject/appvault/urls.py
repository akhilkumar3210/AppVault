from django.apps import AppConfig
from django.urls import path
from . import views
urlpatterns=[
    path('',views.val_login),
    path('register',views.register),
    path('vault',views.vault),
    path('logout',views.val_logout),
    path('addfile/<id>',views.addfile),
    path('del/<id>',views.f_delete),
    
    
]