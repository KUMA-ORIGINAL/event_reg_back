from rest_framework import serializers


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
        team = Team.objects.create(**validated_data)
        TeamCaptain.objects.create(team=team, **captain_data)
        for participant_data in participants_data:
            Participant.objects.create(team=team, **participant_data)
        return team
