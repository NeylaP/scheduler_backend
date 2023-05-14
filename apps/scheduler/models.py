from django.db import models

# Create your models here.
class Vehicle(models.Model):
    description = models.CharField(max_length=500)
    year = models.BigIntegerField(null=True)
    capacity = models.BigIntegerField(null=True)
    make = models.CharField(max_length=50)
    registration_date = models.DateTimeField(auto_now_add=True)
    deletion_date = models.DateTimeField(blank=True, null=True)
    registration_user = models.ForeignKey("general.Users",on_delete=models.PROTECT,related_name="registration_user_vehicles",null=True,)
    deletion_user = models.ForeignKey("general.Users",on_delete=models.PROTECT,related_name="deletion_user_vehicles",null=True,)
    active = models.CharField(choices=[("1", "True"), ("0", "False")], default="1", max_length=10)

class Route(models.Model):
    description = models.CharField(max_length=500)
    driver = models.ForeignKey("general.Users", on_delete=models.PROTECT, null=True, related_name="users_route")
    vehicle = models.ForeignKey("Vehicle", on_delete=models.PROTECT, null=True, related_name="vehicles_route")
    registration_date = models.DateTimeField(auto_now_add=True)
    deletion_date = models.DateTimeField(blank=True, null=True)
    registration_user = models.ForeignKey("general.Users",on_delete=models.PROTECT,related_name="registration_user_route",null=True,)
    deletion_user = models.ForeignKey("general.Users", on_delete=models.PROTECT, related_name="deletion_user_route", null=True)
    active = models.CharField(choices=[("1", "True"), ("0", "False")], default="1", max_length=10)

class Schedules(models.Model):
    route = models.ForeignKey("Route", on_delete=models.PROTECT, null=True, related_name="users_route")
    week_num = models.BigIntegerField(null=True)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    deletion_date = models.DateTimeField(blank=True, null=True)
    registration_user = models.ForeignKey("general.Users",on_delete=models.PROTECT,related_name="registration_user_schedules",null=True,)
    deletion_user = models.ForeignKey("general.Users", on_delete=models.PROTECT, related_name="deletion_user_schedules", null=True,)
    active = models.CharField(choices=[("1", "True"), ("0", "False")], default="1", max_length=10)
