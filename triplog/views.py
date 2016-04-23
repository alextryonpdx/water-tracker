from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from . import forms
from .models import Entry, Guide
from .forms import GuideForm#, SortDate



def entries_list(request):
	entryList = Entry.objects.all()
	return render(request, 'triplog/entries_list.html', {'entryList': entryList})

def guide_list(request):
	guideList = Guide.objects.all()
	return render(request, 'triplog/guide_list.html', {'guideList': guideList})

def single_guide(request, pk):
	guide = get_object_or_404(Guide, pk=pk)
	entryList = Entry.objects.filter(guide=guide)
	return render(request, 'triplog/single_guide.html', {'entryList': entryList, 'guide': guide })

def single_trip(request, pk):
	trip = get_object_or_404(Entry, pk=pk)
	return render(request, 'triplog/single_trip.html', {'trip': trip})

def guide_new(request):
	if request.method == "POST":
		form = GuideForm(request.POST)
		if form.is_valid():
			guide = form.save(commit=False)
			guide.save()
			return redirect('single_guide', pk=guide.pk)
	else:
		form = GuideForm()
		return render(request, 'triplog/guide_edit.html', {'form': form})

# need to work through this. create form to link to this page.
	# will need to send info for guide, start and end date
	#  will need to create new template with spreadsheet view sorted like the payroll trip log
def single_guide_filtered(request, pk, S, E):
	startTime = S
	endTime = E
	guide = get_object_or_404(Guide, pk=pk)
	entryList = Entry.objects.filter(guide=guide, date__gte=startTime, date__lte=endTime)
	return render(request, 'triplog/single_guide.html', {'entryList': entryList, 'guide': guide })



def SortView(request):
	form = forms.SortDate()
	if request.method == 'POST':
		form = forms.SortDate(request.POST)
		if form.is_valid:
			print('good form')
	return render(request, 'triplog/sort.html', {'form' : form})