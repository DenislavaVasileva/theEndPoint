from django.contrib import admin
from unfold.admin import ModelAdmin
from theEndPoint.peaks.models import Peak


@admin.register(Peak)
class PeakAdmin(ModelAdmin):
    list_display = ['name', 'elevation', 'mountain_range', 'description']
    list_filter = ['mountain_range']