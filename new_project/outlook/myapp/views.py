from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .auth_helper import (
    get_sign_in_flow, get_token_from_code,
    store_user, remove_user_and_token, get_token
)
from myapp.graph_helper import get_user
from msal import ConfidentialClientApplication
from rest_framework import generics
from .models import UserAccount
from .serializers import UserAccountSerializer

class UserAccountListView(generics.ListCreateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

class UserAccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer


def home(request):
    context = initialize_context(request)
    return render(request, 'account/home.html', context)


def initialize_context(request):
    context = {}
    error = request.session.pop('flash_error', None)
    if error is not None:
        context['errors'] = []
        context['errors'].append(error)
    # Check for user in the session
    context['user'] = request.session.get('user', {'is_authenticated': False})
    return context


def sign_in(request):
    # Get the sign-in flow
    flow = get_sign_in_flow()
    # Save the expected flow so we can use it in the callback
    try:
        request.session['auth_flow'] = flow
    except Exception as e:
        print(e)
    # Redirect to the Azure sign-in page
    return HttpResponseRedirect(flow['auth_uri'])


def sign_out(request):
    # Clear out the user and token
    remove_user_and_token(request)
    return HttpResponseRedirect(reverse('home'))


def callback(request):
    # Make the token request
    result = get_token_from_code(request)
    # Get the user's profile from graph_helper.py script
    user = get_user(result['access_token']) 
    # Store user from auth_helper.py script
    store_user(request, user)
    return HttpResponseRedirect(reverse('home'))

