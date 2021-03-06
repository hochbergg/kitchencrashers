from django.db import models
from django.db.models.signals import post_save
from django_facebook.models import FacebookCustomUser
from kitchencrashers import settings

COOK = 'Cook'
CLEANER = 'Cleaner'

class RsvpOptions():
	COOK = 'Cook'
	CLEANER = 'Cleaner'
	RSVP_OPTIONS = ((1,COOK,), (2,CLEANER,))

	def get_rsvp_by_id(self, id):
		for option in self.RSVP_OPTIONS:
			if (option[0] == id):
				return option[1]
		return -1

class CategoryOptions():
	CATEGORY_OPTIONS = (
		(1,'Italian'),
		(2, 'Japaneese'),
		(3, 'Asian'),
		(4, 'Mediteranian'))

	def get_category_by_id(self, id):
		for option in self.CATEGORY_OPTIONS:
			if (option[0] == id):
				return option[1]
		return -1


# Create your models here.
class Event(models.Model):
	name = models.TextField()
	date = models.DateTimeField()
	location = models.TextField()
	city = models.TextField()
	category = models.TextField()
	description = models.TextField()
	budget = models.IntegerField()
	max_people = models.IntegerField(blank=True, null=True)
	is_vegan = models.BooleanField()
	is_kosher = models.BooleanField()
	is_vegeterian = models.BooleanField()
	picture = models.ImageField(upload_to='event_pics', blank=True, null=True)
	organizer = models.ForeignKey("KitchenUser",related_name="organizing")
	
	def get_num_cooks(self):
		return self.participants.filter(rsvp = COOK).count()
	num_cooks = property(get_num_cooks)
	
	def get_num_cleaners(self):
		return self.participants.filter(rsvp = CLEANER).count()
	num_cleaners = property(get_num_cleaners)

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
