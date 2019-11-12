from django.shortcuts import render
from django.views.generic import ListView
from tracker.models import Entry
from tracker.models import EntryLookup

# print(EntryLookup)

def dashboard(request):
	# only entries for current user should show
	workouts = Entry.objects.filter(author_id = request.user.id).order_by('-date_posted')
	entries = EntryLookup.objects.filter(entry_id__in=workouts)
	context = {
		'workouts': workouts,
		'entries': entries
	}

	return render(request, 'tracker/dashboard.html', context)

class DashboardView(ListView):
	model = EntryLookup.objects.filter()
	template_name = 'tracker/dashboard.html'
	context_object_name = 'entries'

	def get_context_data(self, **kwargs):
	    context = super(DashboardView, self).get_context_data(**kwargs)
	    data = EntryLookup.objects.all()
	    context.update({'data': data})
	    return context
