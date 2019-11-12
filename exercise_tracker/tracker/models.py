from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Entry(models.Model):
	title = models.CharField(max_length=100)
	time_in_minutes = models.IntegerField(default = 0)
	date_posted = models.DateTimeField(default=timezone.now())
	author = models.ForeignKey(User, on_delete=models.CASCADE)

class Exercise(models.Model):
	name = models.CharField(max_length=100)
	type = models.CharField(
        max_length=7,
        choices=(
            ("lift", "Lift"),
            ("cardio", "Cardio")
        )
    )

class EntryLookup(models.Model):
	entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
	exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
	sets = models.IntegerField(default = 0)
	reps = models.IntegerField(default = 0)

