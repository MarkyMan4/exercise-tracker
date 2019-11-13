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
	entry = models.ForeignKey(Workout, on_delete=models.CASCADE)
	exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
	sets = models.IntegerField(default = 0)

