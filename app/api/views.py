import logging

from django.conf import settings
from django.core.mail import send_mail
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from api.serializers import TeamSerializer

logger = logging.getLogger(__name__)

class RegisterTeamView(viewsets.GenericViewSet,
                       mixins.CreateModelMixin):
    serializer_class = TeamSerializer

    def perform_create(self, serializer):
        team = serializer.save()

        # Отправка email
        subject = 'Регистрация команды'
        message = f'Команда {team.name} успешно зарегистрирована.'
        recipient_list = [team.captain.email]
        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                recipient_list,
                fail_silently=False
            )
        except Exception as e:
            # Логируем ошибку отправки email
            logger.error(f"Ошибка отправки email: {e}")
            # Можем также добавить уведомление администратору о неудачной отправке email, если нужно

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
