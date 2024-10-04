from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth.models import User
from rest_framework import viewsets

from shop.models import Category, Product, Order
from api.serializers import UserSerializer, CategorySerializer, ProductSerializer, OrderSerializer


class RegisterTeamView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            team = serializer.save()

            # Отправка email
            subject = 'Регистрация команды'
            message = f'Команда {team.name} успешно зарегистрирована.'
            recipient_list = [team.captain.email] + [p['email'] for p in
                                                     request.data['participants']]
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)