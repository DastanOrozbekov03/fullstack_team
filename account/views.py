from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from .serializers import RegisterSerializer, ForgotPasswordSerializer, ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated



User = get_user_model()


class RegisterView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data) # request хранится то что нам передал пользаватель
        serializer.is_valid(raise_exception=True)
        serializer.save()#под капотом есть метод create
        return Response('Вы успешно прошли регистрацию', status=201)
    

class ActivationView(APIView):
    def get(self, request, email, activation_code):
        user = User.objects.filter(email=email, activation_code=activation_code).first()
        if not user:
            return Response(
                'Пользователь не найден'
            )
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response(
            'Аккаунт успешно активирован', status=200
        )


class ForgotPasswordView(APIView):
    @swagger_auto_schema(request_body=ForgotPasswordSerializer())

    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.gen_new_password()
        return Response(
            'Новый пароль отправлен вам на почту'

        )
    

class ChangePasswordView(APIView):

    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(request_body=ChangePasswordSerializer())

    
    def patch(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response(
            'Пароль успешно изменен'
        )

