from django.contrib import admin
from .models import Contact, Subscribe


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
