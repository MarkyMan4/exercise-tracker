from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Workout(models.Model):
	title = models.CharField(max_length=100)
	time_in_minutes = models.IntegerField(default = 0)
	workout_date = models.DateTimeField(default=timezone.now())
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

class Entry(models.Model):
	workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
	exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
	sets = models.IntegerField(default = 0)

class Plan(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	SUNDAY = 'SUNDAY'
	MONDAY = 'MONDAY'
	TUESDAY = 'TUESDAY'
	WEDNESDAY = 'WEDNESDAY'
	THURSDAY = 'THURSDAY'
	FRIDAY = 'FRIDAY'
	SATURDAY = 'SATURDAY'

	DAY_CHOICES = (
		(SUNDAY, 'Sunday'),
		(MONDAY, 'Monday'),
		(TUESDAY, 'Tuesday'),
		(WEDNESDAY, 'Wednesday'),
		(THURSDAY, 'Thursday'),
		(FRIDAY, 'Friday'),
		(SATURDAY, 'Saturday')
	)

	day = models.CharField(max_length=9, choices=DAY_CHOICES)
	exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
