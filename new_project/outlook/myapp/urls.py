from django.urls import path
from . import views
from .views import UserAccountListView, UserAccountDetailView


urlpatterns = [
    path('useraccounts/', UserAccountListView.as_view(), name='useraccount-list'),
    path('useraccounts/<int:pk>/', UserAccountDetailView.as_view(), name='useraccount-detail'),
    path('', views.home, name='home'),
    path('signin', views.sign_in, name='signin'),
    path('signout', views.sign_out, name='signout'),
    path('callback', views.callback, name='callback'),
    # path('login', views.outlook_login, name='outlook_login'),
]
