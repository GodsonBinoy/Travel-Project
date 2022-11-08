from django.urls import path
from . import views
urlpatterns = [
    path('newuser/',views.reg, name='reg'),
    path('login/',views.login,name='login'),
    path('logout',views.logout,name='logout'),
]

