import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render
from academic.models import *


# Create your views here.
def calender(request):
    calender_img = UploadCalender.objects.all()
    return render(request, 'calender.html', {'calender_img': calender_img})


def timeTable(request):
    tt_all = TimeTable.objects.all()
    return render(request, 'timetable.html', {'tt_all': tt_all})


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def semOne(request):
    sem_one_pdfs = SemOne.objects.all()
    return render(request, 'notes.html', {'sem_one_pdfs': sem_one_pdfs})

def semTwo(request):
    sem_two_pdfs = SemTwo.objects.all()
    return render(request, 'notes.html', {'sem_two_pdfs': sem_two_pdfs})

def semThree(request):
    sem_Three_pdfs = SemThree.objects.all()
    return render(request, 'notes.html', {'sem_Three_pdfs': sem_Three_pdfs})

def semFour(request):
    sem_Four_pdfs = SemFour.objects.all()
    return render(request, 'notes.html', {'sem_Four_pdfs': sem_Four_pdfs})

def semFive(request):
    sem_Five_pdfs = SemFive.objects.all()
    return render(request, 'notes.html', {'sem_Five_pdfs': sem_Five_pdfs})

def semSix(request):
    sem_Six_pdfs = SemSix.objects.all()
    return render(request, 'notes.html', {'sem_Six_pdfs': sem_Six_pdfs})

def semSeven(request):
    sem_Seven_pdfs = SemSeven.objects.all()
    return render(request, 'notes.html', {'sem_Seven_pdfs': sem_Seven_pdfs})

def semEight(request):
    sem_Eight_pdfs = SemEight.objects.all()
    return render(request, 'notes.html', {'sem_Eight_pdfs': sem_Eight_pdfs})