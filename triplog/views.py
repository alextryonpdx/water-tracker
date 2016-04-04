from django.shortcuts import render




def entries_list(request):
    return render(request, 'triplog/entries_list.html', {})
