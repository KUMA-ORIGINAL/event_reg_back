from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=255, unique=True)
    university = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

    def __str__(self):
        return self.name

class Participant(models.Model):
    team = models.ForeignKey(Team, related_name='participants', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    role = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

    def __str__(self):
        return self.full_name

class TeamCaptain(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name='captain')
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=100, choices=[('leader', 'Leader'), ('other', 'Other')], default='leader')
    age = models.IntegerField()

    class Meta:
        verbose_name = 'Капитан'
        verbose_name_plural = 'Капитаны'

    def __str__(self):
        return self.full_name
