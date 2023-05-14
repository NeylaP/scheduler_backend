from django.urls import path

from .viewsets import CreateUser, Login, current_user

apiv1 = "api/v1.0/"

urlpatterns = [
    path("current_user", current_user),
    path("validar_credenciales", Login.as_view(), name=None),
    path("drivers_scheduler/crear_user", CreateUser.as_view(), name=None),
]
