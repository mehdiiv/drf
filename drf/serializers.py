from rest_framework import serializers
from decouple import config
from rest_framework.exceptions import AuthenticationFailed
from api.models import User, Message
from api.common_methods import create_jwt
from api.common_methods import authorization
import jwt

JWT_SECRET_KEY = config('JWT_SECRET_KEY')

def authorizationdrf(bearer_token):
    load_data = jwt.decode(
            bearer_token[7:], JWT_SECRET_KEY, algorithms=["HS256"]
            )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'json_web_token')
        read_only_fields = ('json_web_token', )

    def create(self, validated_data):
        jwt_token = create_jwt(validated_data['email'])
        validated_data['json_web_token'] = jwt_token
        return super().create(validated_data)

class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=True)
    class Meta:
        model = Message
        fields = ('title', 'body')

    def create(self, validated_data):
        request = self.context['request']
        bearer_token = request.headers.get('Authorization')
        try:
            user_data = authorizationdrf(bearer_token)
            user = User.objects.get(email=user_data['email']).id
        except AuthenticationFailed:
            raise AuthenticationFailed('Invalid token')
        validated_data['user'] = user

        return super().create(validated_data)
