from django.shortcuts import render

# Create your views here.

def project_list(request):
    return render(request, 'NEW_START/project_list.html', {})

'''def calendarplan_list(request):
    return render(request, 'NEW_START/calendarplan_list.html', {})

def task_list(request):
    return render(request, 'NEW_START/task_list.html', {})'''