from django import forms
from django.forms import ModelForm
from .models import Workout, Exercise, Entry


class WorkoutCreateForm(ModelForm):
	title = forms.CharField(max_length=100)
	workout_date = forms.DateTimeField(
		widget=forms.SelectDateWidget(),
	)
	time_in_minutes = forms.IntegerField()

	class Meta:
		model = Workout
		fields = ['title', 'workout_date', 'time_in_minutes']

def get_exercise_options():
	exercises = Exercise.objects.all().values()
	options = []

	for i in range(len(exercises)):
		options.append((exercises[i]['id'], exercises[i]['name']))

	return options

class EntryCreateForm(ModelForm):
	exercise = forms.CharField(
		label="Select an exercise",
		widget=forms.Select(choices=get_exercise_options())
	)

	class Meta:
		model = Entry
		fields = ['sets']