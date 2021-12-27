from django.contrib import admin
from .models import UltrasonicSensor, CameraSensor

class USAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(UltrasonicSensor, USAdmin)
admin.site.register(CameraSensor)
