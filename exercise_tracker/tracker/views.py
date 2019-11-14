from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView
from tracker.models import Entry
from tracker.models import Workout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django import forms
from .forms import WorkoutCreateForm
from django.views.generic.edit import FormView
from datetime import datetime


def dashboard(request):
	# only entries for current user should show
	workouts = Workout.objects.filter(author_id = request.user.id).order_by('-workout_date')
	entries = Entry.objects.filter(entry_id__in=workouts)
	context = {
		'workouts': workouts,
		'entries': entries
	}

	return render(request, 'tracker/dashboard.html', context)

def workout_create(request):
	auth_id = request.session['_auth_user_id']

	if request.method == 'POST':
		form = WorkoutCreateForm(request.POST)
		if form.is_valid():
			workout = form.save(commit=False)
			workout.author_id = auth_id
			workout.save()
			return redirect('entry/' + str(workout.id))

	context = {
		'form': WorkoutCreateForm(initial={'workout_date': datetime.now()})
	}
	return render(request, 'tracker/workout_new.html', context)

def entry_create(request, id=None):
	# auth_id = request.session['_auth_user_id']

	# if request.method == 'POST':
	# 	form = WorkoutCreateForm(request.POST)
	# 	if form.is_valid():
	# 		workout = form.save(commit=False)
	# 		workout.author_id = auth_id
	# 		workout.save()
	# 		messages.success(request, 'Workout created!')
	# 		return redirect('tracker-dashboard')

	# context = {
	# 	'form': WorkoutCreateForm(initial={'workout_date': datetime.now()})
	# }
	# id = request.GET.get('id')

	context = {
		'id': id
	}

	return render(request, 'tracker/add_exercises.html', context)
	
