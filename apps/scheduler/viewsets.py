
import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import status
from ..general.models import Users
from .serializers import RouteSerializer, RouteSerializerList, ShedulesSerializer, ShedulesSerializerList, VehicleSerializer, VehicleSerializerList
from .models import Route, Schedules, Vehicle

# Vehicles

class CreateVehicle(generics.CreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def create(self, request, *args, **kwargs):
        (user, token) = JSONWebTokenAuthentication().authenticate(request)
        _mutable = request.data._mutable
        request.data._mutable = True
        required_fields = ['make', 'year', 'description', 'capacity']
        for field in required_fields:
            if not request.data.get(field):
                return Response({"titulo": f"{field} es un campo requerido"}, status=status.HTTP_400_BAD_REQUEST)
        request.data["registration_user"]=user.id
        request.data._mutable = _mutable
        super(CreateVehicle, self).create(request, args, kwargs)
        return Response({"titulo": "Success"})

class ListVehicles(generics.ListAPIView):
    queryset = Vehicle.objects.filter(active=1)
    serializer_class = VehicleSerializerList
    
class DeleteVehicle(generics.UpdateAPIView):
    def update(self, request, pk):
        try:
            vehicle = Vehicle.objects.get(pk=pk)
        except (KeyError, Vehicle.DoesNotExist):
            return Response({"titulo": "el dato no existe"}, status=status.HTTP_302_FOUND)
        else:
            (usuario, token) = JSONWebTokenAuthentication().authenticate(request)
            vehicle.active = 0
            vehicle.deletion_date = datetime.datetime.now()
            vehicle.deletion_user = Users.objects.get(pk=4)
            vehicle.save()
            return Response({"titulo": "Success"})
        
class UpdateVehicle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def patch(self, request, *args, **kwargs):
        (usuario, token) = JSONWebTokenAuthentication().authenticate(request)
        try:
            vehicle = Vehicle.objects.get(pk=kwargs['pk'])
        except (KeyError, Vehicle.DoesNotExist):
            return Response({"titulo": "Dato no encontrado"},
                            status=status.HTTP_302_FOUND)
        else:
            super(UpdateVehicle, self).patch(request, args, kwargs)
            return Response({"titulo": "success"})

# Routes

class CreateRoute(generics.CreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    def create(self, request, *args, **kwargs):
        (user, token) = JSONWebTokenAuthentication().authenticate(request)
        _mutable = request.data._mutable
        request.data._mutable = True
        required_fields = ['vehicle', 'driver', 'description']
        for field in required_fields:
            if not request.data.get(field):
                return Response({"titulo": f"{field} es un campo requerido"}, status=status.HTTP_400_BAD_REQUEST)
        request.data["registration_user"]=user.id
        request.data._mutable = _mutable
        super(CreateRoute, self).create(request, args, kwargs)
        return Response({"titulo": "Success"})

class ListRoutes(generics.ListAPIView):
    queryset = Route.objects.filter(active=1)
    serializer_class = RouteSerializerList
    
class DeleteRoute(generics.UpdateAPIView):
    def update(self, request, pk):
        try:
            route = Route.objects.get(pk=pk)
        except (KeyError, Route.DoesNotExist):
            return Response({"titulo": "el dato no existe"}, status=status.HTTP_302_FOUND)
        else:
            (usuario, token) = JSONWebTokenAuthentication().authenticate(request)
            route.active = 0
            route.deletion_date = datetime.datetime.now()
            route.deletion_user = Users.objects.get(pk=4)
            route.save()
            return Response({"titulo": "Success"})
        
class UpdateRoute(generics.RetrieveUpdateDestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    def patch(self, request, *args, **kwargs):
        (usuario, token) = JSONWebTokenAuthentication().authenticate(request)
        try:
            route = Route.objects.get(pk=kwargs['pk'])
        except (KeyError, Route.DoesNotExist):
            return Response({"titulo": "Dato no encontrado"},
                            status=status.HTTP_302_FOUND)
        else:
            super(UpdateRoute, self).patch(request, args, kwargs)
            return Response({"titulo": "success"})
# Shedules

class CreateSchedule(generics.CreateAPIView):
    queryset = Schedules.objects.all()
    serializer_class = ShedulesSerializer

    def create(self, request, *args, **kwargs):
        (user, token) = JSONWebTokenAuthentication().authenticate(request)
        _mutable = request.data._mutable
        request.data._mutable = True
        required_fields = ['route', 'to_date', 'from_date', 'week_num']
        for field in required_fields:
            if not request.data.get(field):
                return Response({"titulo": f"{field} es un campo requerido"}, status=status.HTTP_400_BAD_REQUEST)
        request.data["registration_user"]=user.id
        request.data._mutable = _mutable
        super(CreateSchedule, self).create(request, args, kwargs)
        return Response({"titulo": "Success"})

class ListSchedules(generics.ListAPIView):
    queryset = Schedules.objects.filter(active=1)
    serializer_class = ShedulesSerializerList
    
class DeleteSchedule(generics.UpdateAPIView):
    def update(self, request, pk):
        try:
            schedu = Schedules.objects.get(pk=pk)
        except (KeyError, Schedules.DoesNotExist):
            return Response({"titulo": "el dato no existe"}, status=status.HTTP_302_FOUND)
        else:
            (usuario, token) = JSONWebTokenAuthentication().authenticate(request)
            schedu.active = 0
            schedu.deletion_date = datetime.datetime.now()
            schedu.deletion_user = Users.objects.get(pk=4)
            schedu.save()
            return Response({"titulo": "Success"})
        
class UpdateSchedule(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedules.objects.all()
    serializer_class = ShedulesSerializer

    def patch(self, request, *args, **kwargs):
        (usuario, token) = JSONWebTokenAuthentication().authenticate(request)
        try:
            schedu = Schedules.objects.get(pk=kwargs['pk'])
        except (KeyError, Schedules.DoesNotExist):
            return Response({"titulo": "Dato no encontrado"},
                            status=status.HTTP_302_FOUND)
        else:
            super(UpdateSchedule, self).patch(request, args, kwargs)
            return Response({"titulo": "success"})