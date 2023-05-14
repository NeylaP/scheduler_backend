from django.db import models
import os
from uuid import uuid4
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
def path_and_rename(instance, filename):
    upload_to = "attached/parameters"
    ext = filename.split(".")[-1]
    filename = "{}.{}".format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)

class GeneralParameters(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    active = models.CharField( choices=[("1", "True"), ("0", "False")], default="1", max_length=10)

class ValueParameters(models.Model):
    parameter = models.ForeignKey("GeneralParameters",on_delete=models.PROTECT,related_name="parameter_value_parameters",)
    code = models.CharField(max_length=50, blank=True, null=True)
    file = models.FileField(upload_to=path_and_rename, blank=True, null=True)
    name = models.TextField()
    description = models.TextField(max_length=500, blank=True, null=True)
    first_value = models.TextField(blank=True, null=True)
    second_value = models.TextField(blank=True, null=True)
    third_value = models.TextField(blank=True, null=True)
    fourth_value = models.TextField(blank=True, null=True)
    fifth = models.TextField(blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    deletion_date = models.DateTimeField(blank=True, null=True)
    registration_user = models.ForeignKey("Users",on_delete=models.PROTECT,related_name="registration_user_value",null=True,)
    deletion_user = models.ForeignKey("Users", on_delete=models.PROTECT, related_name="deletion_user_value", null=True)
    active = models.CharField(choices=[("1", "True"), ("0", "False")], default="1", max_length=10)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class Users(AbstractBaseUser):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    password = models.TextField(max_length=200)
    profile = models.ForeignKey("ValueParameters", on_delete=models.PROTECT, null=True)
    ssn = models.CharField(max_length=20, unique=True)
    dob = models.DateField(null=True)
    address = models.TextField(max_length=500, null=True)
    city = models.TextField(max_length=50, null=True)
    zip = models.BigIntegerField(null=True)
    phone = models.BigIntegerField(null=True)
    last_login = models.DateTimeField(null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    deletion_date = models.DateTimeField(blank=True, null=True)
    registration_user = models.ForeignKey("Users",on_delete=models.PROTECT,related_name="registration_user_users",null=True,)
    deletion_user = models.ForeignKey("Users", on_delete=models.PROTECT, related_name="deletion_user_users", null=True)
    active = models.CharField(choices=[("1", "True"), ("0", "False")], default="1", max_length=10)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin