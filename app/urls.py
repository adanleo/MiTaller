from django.urls import path

from . import views
'''
    rutas disponibles
'''
urlpatterns = [
    path('login/', views.sign_in, name='login'),
    path('posts/', views.index, name="posts"),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register')
]