from django.db import transaction
from rest_framework import serializers
from rest_auth.serializers import TokenSerializer


from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'location', 'phone_number', 'date_of_birth',
                  'profile_pic', 'employee_jobs')

    def validate(self, attrs):
        image = None
        if self.context['request'].FILES.values():
            image = self.context['request'].FILES.values()
        print("serializers print --------")
        print(attrs)
        return super().validate(attrs)

    def create(self, validated_data):
        with transaction.atomic():
            image = None
            if self.context['request'].FILES.values():
                image = self.context['request'].FILES.values()[0]
            return super().create(image=image, **validated_data)



class TokenWithUserDataSerializer(TokenSerializer):
    """
    LoginSerializer for rest_auth which passes an extra parameter of user
    after login
    """
    def to_representation(self, instance):
        result = super().to_representation(instance=instance)
        result['pk'] = instance.user.pk
        result['username'] = instance.user.username
        return result