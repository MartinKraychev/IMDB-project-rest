from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

UserModel = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):

    # Hash the password in the DB
    def create(self, validated_data):
        user = super(RegisterSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    # Removes the hashed password from the response
    def to_representation(self, instance):
        result = super().to_representation(instance)
        result.pop('password')
        return result

    # Adds password validation
    @staticmethod
    def validate_password(value):
        try:
            validate_password(value)
        except ValidationError as exc:
            raise ValidationError(str(exc))

        return value

    class Meta:
        model = UserModel
        fields = ('username', 'password')
