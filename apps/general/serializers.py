from rest_framework import serializers
from .models import GeneralParameters, Users, ValueParameters


class GenericaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralParameters
        fields = "__all__"


class ValueParametersList(serializers.ModelSerializer):
    parameter = GenericaSerializer(read_only=True)

    class Meta:
        model = ValueParameters
        fields = "__all__"


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class UsersSerializerList(serializers.ModelSerializer):
    profile = ValueParametersList(read_only=True)

    class Meta:
        model = Users
        fields = "__all__"
