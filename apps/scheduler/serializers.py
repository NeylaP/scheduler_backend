from rest_framework import serializers

from ..general.serializers import UsersSerializerList
from .models import Route, Schedules, Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"

class VehicleSerializerList(serializers.ModelSerializer):
    registration_user = UsersSerializerList(read_only=True)

    class Meta:
        model = Vehicle
        fields = "__all__"

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = "__all__"

class RouteSerializerList(serializers.ModelSerializer):
    registration_user = UsersSerializerList(read_only=True)
    driver = UsersSerializerList(read_only=True)
    vehicle = VehicleSerializerList(read_only=True)
    class Meta:
        model = Route
        fields = "__all__"

class ShedulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedules
        fields = "__all__"

class ShedulesSerializerList(serializers.ModelSerializer):
    registration_user = UsersSerializerList(read_only=True)
    route = RouteSerializerList(read_only=True)
    class Meta:
        model = Schedules
        fields = "__all__"