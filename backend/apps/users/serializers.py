from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password')
        extra_kwarg = {'password': {'write_only': True, 'min_length': 8}}


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True,
                                     validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match"})

        return attrs

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        User = get_user_model()

        try:
            User.objects.filter(email=email)
            return
        except User.DoesNotExist:
            user = User.objects.create(email=email)
            user.set_password(password)
            user.save()
            return user
