from django.db.models import Q
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework import permissions, status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
import datetime
from .serializers import UsersSerializer, UsersSerializerList
from .models import Users


@api_view(["GET"])
def current_user(request):
    if request.user.is_authenticated:
        user = Users.objects.get(id=2)
        user.last_login = datetime.datetime.now()
        user.save()
        serializer = UsersSerializerList(request.user)
        return Response(serializer.data)
    else:
        return Response({'message': 'Usuario no autenticado.'}, status=status.HTTP_401_UNAUTHORIZED)

class Login(ObtainJSONWebToken):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
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
        # (user, token) = JSONWebTokenAuthentication().authenticate(request)
        # _mutable = request.data._mutable
        # request.data._mutable = True
        request.data["password"]=make_password(request.data["password"])
        # request.data._mutable = _mutable
        super(CreateUser, self).create(request, args, kwargs)
        return Response({"titulo": "Success"})