from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from user_profile.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = UserProfile
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'age', 'gender', 'height', 'auth_token']
        read_only_fields = ['auth_token']

    def validate_password(self, value):
        return make_password(value)
