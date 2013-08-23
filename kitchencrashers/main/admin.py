from django.contrib import admin
from .models import Event,KitchenUser,EventParticipant

class EventParticipantInline(admin.TabularInline):
	model = EventParticipant

class EventAdmin(admin.ModelAdmin):
    inlines = [EventParticipantInline]

class EventUserInline(admin.TabularInline):
	model = Event
	fk_name = "organizer"

class KitchenUserAdmin(admin.ModelAdmin):
    inlines = [EventUserInline,EventParticipantInline]

admin.site.register(Event, EventAdmin)
admin.site.register(KitchenUser, KitchenUserAdmin)