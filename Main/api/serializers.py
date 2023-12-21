from rest_framework import serializers
from .models import User,Student
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'thumbnail'
        ]



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','stuname','email']