from django.contrib import admin
from theEndPoint.accounts.models import Profile
from unfold.admin import ModelAdmin


@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    list_display = ['user', 'type_of_climber', 'age', 'bio']
    list_filter = ['type_of_climber', 'age']
    search_fields = ['user', 'bio']
