from django.urls import path
from . import views

urlpatterns = [
	path('',views.accounts_default, name='register'),
	path('login', views.login, name='login'),
	path('register', views.register, name='register'),
	path('logout', views.logout, name='logout'),

]
