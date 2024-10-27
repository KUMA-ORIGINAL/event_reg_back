from django.contrib import admin

from registration.email import send_captain_emails
from registration.models import Participant, TeamCaptain, Team


class ParticipantInline(admin.TabularInline):
    model = Participant
    extra = 1  # Позволяет добавлять участников прямо из интерфейса команды
    fields = ('full_name', 'email', 'role', 'age')

class TeamCaptainInline(admin.StackedInline):
    model = TeamCaptain
    fields = ('full_name', 'email', 'phone_number', 'role', 'age')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'university')  # Отображение названий команд и университетов
    search_fields = ('name', 'university')  # Поля для поиска команд
    inlines = [TeamCaptainInline, ParticipantInline]  # Позволяет редактировать капитана и участников
    list_filter = ('university',)  # Фильтр по университету

    def get_participants(self, obj):
        return ", ".join([p.full_name for p in obj.participants.all()])

    get_participants.short_description = "Участники команды"

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'role', 'age', 'team')  # Отображение всех участников
    search_fields = ('full_name', 'email', 'role')  # Поля для поиска участников
    list_filter = ('role', 'team')  # Фильтр по роли и команде
    ordering = ('full_name',)  # Сортировка по имени

@admin.register(TeamCaptain)
class TeamCaptainAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'role', 'age', 'team')  # Отображение капитанов
    search_fields = ('full_name', 'email', 'phone_number')  # Поля для поиска капитанов
    list_filter = ('role', 'team')  # Фильтр по роли и команде
    actions = ['send_email_to_captains']

    def send_email_to_captains(self, request, queryset):
        send_captain_emails(queryset)
        self.message_user(request, 'Письма успешно отправлены капитанам команд.')

    send_email_to_captains.short_description = 'Отправить email капитанам'