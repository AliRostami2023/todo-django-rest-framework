from rest_framework import serializers
from account.models import User


class RegisterSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'full_name': {'required':True},
            'username': {'required':True},
            'email': {'required':True},
            'password': {'required':True, 'write_only':True},
        }

    def validate_username(self, value):
        if value == 'admin':
            raise serializers.ValidationError('username cant be admin!')
        return value
    
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('password and confirm password must match!')
        return data
        
    def validate_email(self, value):
        if value == 'admin':
            raise serializers.ValidationError('email cant be admin')
        return value
    

class UserUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # exra_kwargs = {
        #     'full_name':{'required':True},
        #     'username':{'required':True},
        #     'email':{'required':True},
        # }

