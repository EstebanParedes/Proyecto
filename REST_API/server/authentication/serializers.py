from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .models import customers


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True)
    username = serializers.CharField(
        required=True)
    password = serializers.CharField(
        min_length=8, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password')

    def validate_password(self, value):
        return make_password(value)

    def validate_username(self, value):
        value = value.replace(" ", "")
        try:
            user = get_user_model().objects.get(username=value)
            if user == self.instance:
                return value
        except get_user_model().DoesNotExist:
            return value
        raise serializers.ValidationError("Username ya existe")

    def validate_email(self, value):
        try:
            user = get_user_model().objects.get(email=value)
        except get_user_model().DoesNotExist:
            return value
        raise serializers.ValidationError("Email ya existe")

    def update(self, instance, validated_data):
        validated_data.pop('email', None)              
        return super().update(instance, validated_data) 

class customers_serializer(serializers.ModelSerializer):
        name = serializers.EmailField(
        required=True)
        phone = serializers.CharField(
        required=True)
        email = serializers.CharField(
        write_only=True)

class Meta:
        model=customers
        fields=('name', 'phone', 'email')

def validate_email(self, value):
        try:
            user = get_user_model().objects.get(email=value)
        except get_user_model().DoesNotExist:
            return value
        raise serializers.ValidationError("Email ya existe")

    