from django.urls import path
from scmapp import views

app_name = 'scmapp'

urlpatterns = [
    path('registration',views.index),
    path('user_home/',views.user_home),
    path('test',views.test,name='test'),
    path('login_user',views.login_user,name='login_user'),

    path('admin_login',views.admin_login,name='admin_login'),
    path('login_admin',views.login_admin,name='login_admin'),

    path('admin_home',views.admin_home,name='admin_home'),
    path('user_home',views.user_home,name='user_home'),

    
    path('ground_booking',views.ground_booking,name='ground_booking'),
    path('db_ground_booking',views.db_ground_booking,name='db_ground_booking'),

    path('admin_booking',views.admin_booking,name='admin_booking'),

    path('user_logout',views.user_logout,name='user_logout'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
]
