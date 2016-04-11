from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Entry, Guide



def entries_list(request):
	entryList = Entry.objects.all()
	return render(request, 'triplog/entries_list.html', {'entryList': entryList})

def guide_list(request):
	guideList = Guide.objects.all()
	return render(request, 'triplog/guide_list.html', {'guideList': guideList})

def single_guide(request, pk):
	guide = get_object_or_404(Guide, pk=pk)
	entryList = Entry.objects.filter(guide=guide)
	return render(request, 'triplog/single_guide.html', {'entryList': entryList})

def single_trip(request, pk):
	trip = get_object_or_404(Entry, pk=pk)
	return render(request, 'triplog/single_trip.html', {'trip': trip})
