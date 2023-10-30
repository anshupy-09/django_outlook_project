from rest_framework import serializers
from .models import UserAccount

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'email', 'first_name', 'last_name', 'outlook_access_token', 'outlook_refresh_token']
