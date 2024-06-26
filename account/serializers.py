from rest_framework import serializers
from django.contrib.auth import get_user_model
# from .utils import send_activation_code
from .tasks import send_activation_code_celery
from django.core.mail import send_mail
from django.utils.crypto import get_random_string


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=6, required=True, write_only=True) # write_only -> тоолько для записи

    class Meta:
        model = User
        fields = 'email', 'password', 'password_confirm'

    #для проверки схожи ли пароли
    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password_confirm')

        if p1 != p2:
            raise serializers.ValidationError(
                'Пароли не совпадают'
            )
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_code_celery.delay(user.email, user.activation_code)
        return user
    

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                'Пользователь не найден'
            )
        return email
    
    def gen_new_password(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        new_pass = get_random_string(length=6, allowed_chars='0123456789')
        user.set_password(new_pass)
        user.save()

        send_mail(
            'Восстановление пароля',
            f'Ваш новый пароль : {new_pass}',
            'test@gmail.com',
            [user.email]
        )
