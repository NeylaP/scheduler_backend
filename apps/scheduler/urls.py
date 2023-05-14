from django.urls import path

from .viewsets import CreateRoute, CreateSchedule, CreateVehicle, DeleteRoute, DeleteSchedule, DeleteVehicle, ListRoutes, ListSchedules, ListVehicles, UpdateRoute, UpdateSchedule, UpdateVehicle

apiv1 = "api/v1.0/"

urlpatterns = [
    path("vehicles/create", CreateVehicle.as_view(), name=None),
    path("vehicles", ListVehicles.as_view(), name=None),
    path("vehicles/<int:pk>/delete", DeleteVehicle.as_view(), name=None),
    path("vehicles/<int:pk>/update", UpdateVehicle.as_view(), name=None),
    path("routes/create", CreateRoute.as_view(), name=None),
    path("routes", ListRoutes.as_view(), name=None),
    path("routes/<int:pk>/delete", DeleteRoute.as_view(), name=None),
    path("routes/<int:pk>/update", UpdateRoute.as_view(), name=None),
    path("schedules/create", CreateSchedule.as_view(), name=None),
    path("schedules", ListSchedules.as_view(), name=None),
    path("schedules/<int:pk>/delete", DeleteSchedule.as_view(), name=None),
    path("schedules/<int:pk>/update", UpdateSchedule.as_view(), name=None),
]