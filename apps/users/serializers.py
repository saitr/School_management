from django.utils import timezone
from .models import User
from rest_framework import serializers
from django.contrib.auth.hashers import check_password, make_password
from secrets import token_hex
import datetime



class UserSignInSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(read_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)
    token_expires_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = User
        fields = ('user_name', 'email', 'password',
                  'token', 'token_expires_at')
    def create(self, validated_data):
        user = User.objects.filter(email = validated_data['email'])
        if len(user) >0 and validated_data['password'] == user[0].password:
            user[0].token  = token_hex(30)
            user[0].token_expires_at = timezone.now() + datetime.timedelta(days = 7)
            user[0].save()
            return user[0]
         
        else :
            raise serializers.ValidationError(
                {'error':'Invalid email or password '}
            )