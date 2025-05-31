from django.contrib import admin
from django.urls import path
from landing.views import home, signup_view, signin_view, dashboard, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signup/', signup_view, name='signup'),
    path('signin/', signin_view, name='signin'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
]
