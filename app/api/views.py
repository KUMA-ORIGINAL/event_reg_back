from django.conf import settings
from django.core.mail import send_mail
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from api.serializers import TeamSerializer


class RegisterTeamView(viewsets.GenericViewSet,
                       mixins.CreateModelMixin):
    serializer_class = TeamSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            team = serializer.save()

            # Отправка email
            subject = 'Регистрация команды'
            message = f'Команда {team.name} успешно зарегистрирована.'
            recipient_list = [team.captain.email]
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
            except Exception as e:
                return Response({"detail": "Team registered, but failed to send email."},
                                status=status.HTTP_201_CREATED)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
