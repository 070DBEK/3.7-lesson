from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User, UserProfile


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'date_of_birth', 'gender')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Parollar mos kelmadi."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')  # password2 kerak emas
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])  # Parolni hash qilish
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['height', 'weight', 'activity_level', 'goal']


class UserSerializer(serializers.ModelSerializer):
    height = serializers.IntegerField(source='profile.height', required=False)
    weight = serializers.IntegerField(source='profile.weight', required=False)
    activity_level = serializers.CharField(source='profile.activity_level', required=False)
    goal = serializers.CharField(source='profile.goal', required=False)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email',
            'first_name', 'last_name',
            'date_of_birth', 'gender',
            'height', 'weight', 'activity_level', 'goal'
        ]
        extra_kwargs = {
            'username': {'read_only': True},
            'email': {'required': True},
            'first_name': {'required': False},
            'last_name': {'required': False}
        }

    def update(self, instance, validated_data):
        # Profil ma'lumotlarini ajratib olamiz
        profile_data = {
            'height': validated_data.pop('profile.height', None),
            'weight': validated_data.pop('profile.weight', None),
            'activity_level': validated_data.pop('profile.activity_level', None),
            'goal': validated_data.pop('profile.goal', None)
        }

        # User ma'lumotlarini yangilaymiz
        instance = super().update(instance, validated_data)

        # Profil ma'lumotlarini yangilaymiz
        profile, created = UserProfile.objects.get_or_create(user=instance)
        for attr, value in profile_data.items():
            if value is not None:
                setattr(profile, attr, value)
        profile.save()

        return instance