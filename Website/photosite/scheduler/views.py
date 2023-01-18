from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.urls import reverse
import datetime

from .models import Appointment
# Create your views here.
def index(request):
    #display the scheduler page
    error = None
    return render(request, 'scheduler/index.html', {'error':error, 'name':'', 'location':'','email':''})


def make_appointment(request):
    #make the appointment object
    appointment = Appointment()
    appointment.name = request.POST['name']
    appointment.location = request.POST['location']
    appointment.email = request.POST['email']
    appointment.date = request.POST['date']
    appointment.date = datetime.datetime.fromisoformat(appointment.date)
    #make sure no appointments are within 30 minutes of each other
    minuterange = 30
    prior = appointment.date + datetime.timedelta(minutes=-minuterange)
    end = appointment.date + datetime.timedelta(minutes=minuterange)
    conflicting_dates = Appointment.objects.filter(date__range=(prior, end))
    if conflicting_dates:
        #send error.
        return render(request, 'scheduler/index.html', {'error':"The date conflicts with another appointment. Please choose another appointment", 'name':appointment.name, 'location':appointment.location, 'email':appointment.email})
    #if no conflicts, save the date
    appointment.save()
    return render(request, 'scheduler/made.html')

def view_appointment(request, appointment_id):
    #get the appointment, and display it
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    return render(request, 'scheduler/view.html', {'appointment': appointment})

def cancel_appointment(request, appointment_id):
    #get the appointment
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    #remove appointment and display confirmation
    appointment.delete()
    return render(request, 'scheduler/canceled.html')

def cancel_list(request):
    #get the email from the form
    retreived_email = request.POST['email']
    #look for matching emails appointments, and display them
    appointments = Appointment.objects.filter(email=retreived_email)
    return render(request, 'scheduler/cancel_list.html', {'appointments':appointments})
    