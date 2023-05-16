from django.db.models import Q
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import generics, status
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework import permissions, status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
import datetime
from .serializers import GenericaSerializer, UsersSerializer, UsersSerializerList, ValueParameterSerializer, ValueParameterSerializerList
from .models import GeneralParameters, Users, ValueParameters

# USERS

@api_view(["GET"])
def current_user(request):
    if request.user.is_authenticated:
        user = Users.objects.get(id=request.user.id)
        user.last_login = datetime.datetime.now()
        user.save()
        serializer = UsersSerializerList(request.user)
        return Response(serializer.data)
    else:
        return Response({'message': 'Usuario no autenticado.'}, status=status.HTTP_401_UNAUTHORIZED)

class Login(ObtainJSONWebToken):

    permission_classes = (permissions.AllowAny,)
    def post(self, request, *args, **kwargs):
        required_fields = ['email', 'password']
        for field in required_fields:
            if not request.data.get(field):
                return Response({"titulo": f"{field} es un campo requerido"}, status=status.HTTP_400_BAD_REQUEST)
        email = request.data["email"]
        password = request.data["password"]
        
        no_valido = Response(
            {"titulo": "Email o clave incorrectos."},
            status=status.HTTP_302_FOUND,
        )
        try:
            user = Users.objects.get(active=1, email=email)
        except (KeyError, Users.DoesNotExist):
            return Response(
                {
                    "titulo": "Email no registrado",
                    "show_modal": True,
                },
                status=status.HTTP_302_FOUND,
            )
        else:
            response = super().post(request, *args, **kwargs)
            if check_password(password, user.password):
                return response
            return no_valido

class CreateUser(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def create(self, request, *args, **kwargs):
        (user, token) = JSONWebTokenAuthentication().authenticate(request)
        try:
            perfil = ValueParameters.objects.get(code="driver_user")
            user = Users.objects.get((Q(ssn=request.data["ssn"]) | Q(email=request.data["email"])) & Q(active=1))
        except (KeyError, Users.DoesNotExist):
            _mutable = request.data._mutable
            request.data._mutable = True
            required_fields = ['ssn', 'last_name', 'first_name', 'dob', 'city', 'zip', 'phone', 'address', 'email']
            for field in required_fields:
                if not request.data.get(field):
                    return Response({"titulo": f"{field} es un campo requerido"}, status=status.HTTP_400_BAD_REQUEST)
            request.data["password"]=make_password(request.data["ssn"])
            request.data["profile"]=perfil.id
            request.data["registration_user"]=user.id
            request.data._mutable = _mutable
            super(CreateUser, self).create(request, args, kwargs)
            return Response({"titulo": "Success"})
        else:
            return Response({"titulo": "Este usuario ya se encuentra registrado"})
class ListUsers(generics.ListAPIView):
    perfil = ValueParameters.objects.get(code="driver_user")
    queryset = Users.objects.filter(profile=perfil.id, active=1)
    serializer_class = UsersSerializerList

class DeleteUser(generics.UpdateAPIView):
    def update(self, request, pk):
        try:
            user = Users.objects.get(pk=pk)
        except (KeyError, Users.DoesNotExist):
            return Response(
                {"titulo": "La user no existe"}, status=status.HTTP_302_FOUND
            )
        else:
            (usuario, token) = JSONWebTokenAuthentication().authenticate(request)
            user.active = 0
            user.deletion_date = datetime.datetime.now()
            user.deletion_user = Users.objects.get(pk=usuario.id)
            user.save()
            return Response({"titulo": "Success"})
        
class UpdateUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def patch(self, request, *args, **kwargs):
        (usuario, token) = JSONWebTokenAuthentication().authenticate(request)
        try:
            user = Users.objects.get(pk=kwargs['pk'])
        except (KeyError, Users.DoesNotExist):
            return Response({"titulo": "Dato no encontrado"},
                            status=status.HTTP_302_FOUND)
        else:
            super(UpdateUser, self).patch(request, args, kwargs)
            return Response({"titulo": "success"})
        
# GeneralParameters
class CreateGeneralParameter(generics.CreateAPIView):
    queryset = GeneralParameters.objects.all()
    serializer_class = GenericaSerializer

    def create(self, request, *args, **kwargs):
        (usuario, token) = JSONWebTokenAuthentication().authenticate(request)
        _mutable = request.data._mutable
        request.data._mutable = True
        request.data._mutable = _mutable
        super(CreateGeneralParameter, self).create(request, args, kwargs)
        return Response({"titulo": "Success"})

class ListGeneralParameters(generics.ListAPIView):
    queryset = GeneralParameters.objects.filter(active=1)
    serializer_class = GenericaSerializer
class DeleteGeneralParameters(generics.UpdateAPIView):
    def update(self, request, pk):
        try:
            general = GeneralParameters.objects.get(pk=pk)
        except (KeyError, GeneralParameters.DoesNotExist):
            return Response(
                {"titulo": "el dato no existe"}, status=status.HTTP_302_FOUND
            )
        else:
            (usuario, token) = JSONWebTokenAuthentication().authenticate(request)
            general.active = 0
            general.save()
            return Response({"titulo": "Success"})
        
class UpdateGeneralParameters(generics.RetrieveUpdateDestroyAPIView):
    queryset = GeneralParameters.objects.all()
    serializer_class = GenericaSerializer

    def patch(self, request, *args, **kwargs):
        (usuario, token) = JSONWebTokenAuthentication().authenticate(request)
        try:
            user = GeneralParameters.objects.get(pk=kwargs['pk'])
        except (KeyError, GeneralParameters.DoesNotExist):
            return Response({"titulo": "Dato no encontrado"},
                            status=status.HTTP_302_FOUND)
        else:
            super(UpdateGeneralParameters, self).patch(request, args, kwargs)
            return Response({"titulo": "success"})
        
# ValueParameters
class CreateValueParameters(generics.CreateAPIView):
    queryset = ValueParameters.objects.all()
    serializer_class = ValueParameterSerializer

    def create(self, request, *args, **kwargs):
        (usuario, token) = JSONWebTokenAuthentication().authenticate(request)
        _mutable = request.data._mutable
        request.data._mutable = True        
        request.data["registration_user"]=Users.objects.get(pk=usuario.id)
        request.data._mutable = _mutable
        super(CreateValueParameters, self).create(request, args, kwargs)
        return Response({"titulo": "Success"})

class ListValueParameters(generics.ListAPIView):
    queryset = ValueParameters.objects.filter(active=1)
    serializer_class = ValueParameterSerializerList
    
class DeleteValueParameters(generics.UpdateAPIView):
    def update(self, request, pk):
        try:
            value = ValueParameters.objects.get(pk=pk)
        except (KeyError, ValueParameters.DoesNotExist):
            return Response({"titulo": "el dato no existe"}, status=status.HTTP_302_FOUND)
        else:
            # (usuario, token) = JSONWebTokenAuthentication().authenticate(request)
            value.active = 0
            value.deletion_date = datetime.datetime.now()
            value.deletion_user = Users.objects.get(pk=4)
            value.save()
            return Response({"titulo": "Success"})
        
class UpdateValueParameters(generics.RetrieveUpdateDestroyAPIView):
    queryset = ValueParameters.objects.all()
    serializer_class = ValueParameterSerializer

    def patch(self, request, *args, **kwargs):
        (usuario, token) = JSONWebTokenAuthentication().authenticate(request)
        try:
            user = ValueParameters.objects.get(pk=kwargs['pk'])
        except (KeyError, ValueParameters.DoesNotExist):
            return Response({"titulo": "Dato no encontrado"},
                            status=status.HTTP_302_FOUND)
        else:
            super(UpdateValueParameters, self).patch(request, args, kwargs)
            return Response({"titulo": "success"})