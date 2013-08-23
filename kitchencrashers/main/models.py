from django.db import models
from django.db.models.signals import post_save
from django_facebook.models import FacebookCustomUser
from kitchencrashers import settings

# Create your models here.
class Event(models.Model):
	name = models.TextField()
	date = models.DateTimeField()
	location = models.TextField()
	is_vegan = models.BooleanField()
	is_kosher = models.BooleanField()
	is_vegeterian = models.BooleanField()
	organizer = models.ForeignKey("KitchenUser",related_name="orgainizing")

class EventParticipant(models.Model):
	user = models.ForeignKey("KitchenUser",related_name="participating")
	event = models.ForeignKey("Event",related_name="participants")
	rsvp = models.TextField()

class KitchenUser(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	
	def __str__(self):
		return str(self.user.facebook_name)

#Make sure we create a UserProfile when creating a User
def create_facebook_profile(sender, instance, created, **kwargs):
	if created:
		KitchenUser.objects.create(user=instance)

post_save.connect(create_facebook_profile, sender=FacebookCustomUser)
