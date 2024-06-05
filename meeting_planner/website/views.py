from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from meetings.models import Meeting


def welcome(request):
    # return HttpResponse("Welcome to the Meeting Planner!")
    return render(request, "website/welcome.html",
                  # {"num_meetings": Meeting.objects.count()}
                  # )
                  {"meetings": Meeting.objects.all()}
                  )

def date(request):
    return HttpResponse("This page was server at " + str(datetime.now()))

def about(request):
    return HttpResponse("This is Ahmed Taimoor")