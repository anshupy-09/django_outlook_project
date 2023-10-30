"""
URL configuration for outlook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')), 
    path('accounts/', include('allauth.urls')),
    path(' ',TemplateView.as_view(template_name='accounts/login.html'),name='login'),

    
    path('home/', TemplateView.as_view(template_name='dashboard/home.html'), name = 'home'),
    
    path('login/', TemplateView.as_view(template_name='account/login.html'), name = 'login'),
    path('base/', TemplateView.as_view(template_name='account/base.html'), name = 'base'),
    path('email/', TemplateView.as_view(template_name='account/email.html'), name = 'email'),
    path('logout/', TemplateView.as_view(template_name='account/logout.html'), name = 'logout'),
    path('signup/', TemplateView.as_view(template_name='account/signup.html'), name = 'signup'),
    
    path('connections/', TemplateView.as_view(template_name='socialaccount/connections.html'), name = 'connections'),
    path('signup/', TemplateView.as_view(template_name='socialaccount/signup.html'), name = 'signup'),
    path('provider_list/', TemplateView.as_view(template_name='socialaccount/snippets/provider_list.html'), name = 'provider_list'),



]
