from django import forms
from django.forms import ModelForm
from .models import Workout


class WorkoutCreateForm(ModelForm):
	title = forms.CharField(max_length=100)
	workout_date = forms.DateTimeField(
		widget=forms.SelectDateWidget(),
	)
	time_in_minutes = forms.IntegerField()

	class Meta:
		model = Workout
		fields = ['title', 'workout_date', 'time_in_minutes']

class EntryCreateForm(ModelForm):
	entry = forms

	class Meta:
		model = Workout
		fields = ['title', 'workout_date', 'time_in_minutes']