from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
  password = serializers.CharField()
  password2 = serializers.CharField(write_only=True)
  class Meta:
    model = User
    fields = ['email', 'username', 'password', 'password2']

  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      return serializers.ValidationError('Password do not match')
    return attrs

  def create(self, validated_data):
    validated_data.pop('password2')
    user = User.objects.create_user(**validated_data)
    return user

class UserLoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()