from django.urls import path

from .viewsets import CreateGeneralParameter, CreateUser, CreateValueParameters, DeleteGeneralParameters, DeleteUser, DeleteValueParameters, ListGeneralParameters, ListUsers, ListValueParameters, Login, UpdateGeneralParameters, UpdateUser, UpdateValueParameters, current_user

apiv1 = "api/v1.0/"

urlpatterns = [
    path("current_user", current_user),
    path("validar_credenciales", Login.as_view(), name=None),
    path("users/create", CreateUser.as_view(), name=None),
    path("users", ListUsers.as_view(), name=None),
    path("users/<int:pk>/delete", DeleteUser.as_view(), name=None),
    path("users/<int:pk>/update", UpdateUser.as_view(), name=None),
    path("general/create", CreateGeneralParameter.as_view(), name=None),    
    path("general_parameters", ListGeneralParameters.as_view(), name=None),
    path("general/<int:pk>/delete", DeleteGeneralParameters.as_view(), name=None),
    path("general/<int:pk>/update", UpdateGeneralParameters.as_view(), name=None),
    path("value/create", CreateValueParameters.as_view(), name=None),    
    path("value_parameters", ListValueParameters.as_view(), name=None),
    path("value/<int:pk>/delete", DeleteValueParameters.as_view(), name=None),
    path("value/<int:pk>/update", UpdateValueParameters.as_view(), name=None),
]
