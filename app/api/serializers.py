from rest_framework import serializers

from registration.models import Participant, TeamCaptain, Team


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['full_name', 'email', 'role', 'age']


class TeamCaptainSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamCaptain
        fields = ['full_name', 'email', 'phone_number', 'role', 'age']


class TeamSerializer(serializers.ModelSerializer):
    participants = ParticipantSerializer(many=True)
    captain = TeamCaptainSerializer()

    class Meta:
        model = Team
        fields = ['name', 'university', 'participants', 'captain']

    def create(self, validated_data):
        participants_data = validated_data.pop('participants')
        captain_data = validated_data.pop('captain')

        # Сначала создаем команду
        team = Team.objects.create(**validated_data)

        # Теперь создаем капитана и устанавливаем связь с командой
        captain = TeamCaptain.objects.create(team=team, **captain_data)

        # Добавляем участников
        for participant_data in participants_data:
            Participant.objects.create(team=team, **participant_data)

        return team
