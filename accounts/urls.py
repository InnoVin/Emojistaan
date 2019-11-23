from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
#from .views import register_page

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('',include('home.urls')),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('register/',views.register_page,name='register_page'),



]
