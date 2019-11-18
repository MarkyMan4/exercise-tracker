from django.shortcuts import render, redirect
from tracker.models import Entry
from tracker.models import Workout
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .forms import WorkoutCreateForm, EntryCreateForm
from datetime import datetime
from matplotlib import pyplot as plt
from django.db.models import Sum
from django.contrib.auth.decorators import login_required


def get_graph_data(workouts):
	x = []
	y = []
	query_results = workouts.values('workout_date').order_by('workout_date').annotate(total=Sum('time_in_minutes'))

	for i in range(len(query_results)):
		y.append(query_results[i]['total'])
		x.append(query_results[i]['workout_date'].strftime('%Y-%m-%d'))

	return x, y


def dashboard(request):
	# only entries for current user should show
	workouts = Workout.objects.filter(author_id = request.user.id).order_by('-workout_date', '-id')
	entries = Entry.objects.filter(workout_id__in=workouts)

	x, y = get_graph_data(workouts)

	fig = plt.figure(figsize=(4,3))
	plt.bar(x, y)
	plt.xlabel('date')
	plt.ylabel('minutes')
	plt.xticks(rotation=45)
	plt.savefig('media/graphs/graph.png', bbox_inches='tight')

	context = {
		'workouts': workouts,
		'entries': entries
	}

	return render(request, 'tracker/dashboard.html', context)

@login_required
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

@login_required
def entry_create(request, id=None):

	auth_id = int(request.session['_auth_user_id'])
	workout = Workout.objects.filter(id=id).values().first()

	if auth_id != workout['author_id']:
		return render(request, 'tracker/access_denied.html')

	if request.method == 'POST':
		form = EntryCreateForm(request.POST)
		if form.is_valid():
			entry = form.save(commit=False)
			entry.exercise_id = form.cleaned_data['exercise']
			entry.workout_id = id
			entry.save()
			if request.POST.get('save'):
				return redirect('workout-detail', id)

	context = {
		'id': id,
		'form': EntryCreateForm()
	}

	return render(request, 'tracker/add_exercises.html', context)

@login_required
def workout_detail(request, id=None):
	
	if request.GET.get('delete'):
		Entry.objects.filter(id=int(request.GET.get('delete'))).delete()

	auth_id = int(request.session['_auth_user_id'])
	workout = Workout.objects.filter(id=id).values().first()

	if auth_id != workout['author_id']:
		return render(request, 'tracker/access_denied.html')

	title = workout['title']
	time_in_minutes = workout['time_in_minutes']
	date = workout['workout_date']
	entries = Entry.objects.filter(workout_id=id).all()


	context = {
		'id': id,
		'title': title,
		'time_in_minutes': time_in_minutes,
		'date': date,
		'entries': entries,
	}
	return render(request, 'tracker/workout_detail.html', context)
	
