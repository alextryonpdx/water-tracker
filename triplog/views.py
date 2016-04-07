from django.shortcuts import render
from django.utils import timezone
from .models import Entry, Guide



def entries_list(request):
	entryList = Entry.objects.all()
	return render(request, 'triplog/entries_list.html', {'entryList':entryList})
