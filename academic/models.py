from django.db import models


# Create your models here.

class UploadCalender(models.Model):
    title = models.CharField(max_length=100, default='', blank=True)
    description = models.TextField(max_length=200, default='', blank=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to="static/images/", default='')

    def __str__(self):
        return self.title


class TimeTable(models.Model):
    title = models.CharField(max_length=100, default='', blank=True)
    description = models.TextField(max_length=200, default='', blank=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    tt_img = models.ImageField(upload_to="static/images/", default='')

    def __str__(self):
        return self.title

class SemOne(models.Model):
    sub = models.CharField(max_length=100, default='', blank=True)
    name = models.CharField(max_length=100, default='', blank=True)
    year = models.CharField(max_length=100, default='', blank=True)
    pdf_f = models.FileField(upload_to="static/pdfs/", default='', blank=True)

    def __str__(self):
        return self.sub

class SemTwo(models.Model):
    sub = models.CharField(max_length=100, default='', blank=True)
    name = models.CharField(max_length=100, default='', blank=True)
    year = models.CharField(max_length=100, default='', blank=True)
    pdf_f = models.FileField(upload_to="static/pdfs/", default='', blank=True)

    def __str__(self):
        return self.sub

class SemThree(models.Model):
    sub = models.CharField(max_length=100, default='', blank=True)
    name = models.CharField(max_length=100, default='', blank=True)
    year = models.CharField(max_length=100, default='', blank=True)
    pdf_f = models.FileField(upload_to="static/pdfs/", default='', blank=True)

    def __str__(self):
        return self.sub

class SemFour(models.Model):
    sub = models.CharField(max_length=100, default='', blank=True)
    name = models.CharField(max_length=100, default='', blank=True)
    year = models.CharField(max_length=100, default='', blank=True)
    pdf_f = models.FileField(upload_to="static/pdfs/", default='', blank=True)

    def __str__(self):
        return self.sub

class SemFive(models.Model):
    sub = models.CharField(max_length=100, default='', blank=True)
    name = models.CharField(max_length=100, default='', blank=True)
    year = models.CharField(max_length=100, default='', blank=True)
    pdf_f = models.FileField(upload_to="static/pdfs/", default='', blank=True)

    def __str__(self):
        return self.sub

class SemSix(models.Model):
    sub = models.CharField(max_length=100, default='', blank=True)
    name = models.CharField(max_length=100, default='', blank=True)
    year = models.CharField(max_length=100, default='', blank=True)
    pdf_f = models.FileField(upload_to="static/pdfs/", default='', blank=True)

    def __str__(self):
        return self.sub
class SemSeven(models.Model):
    sub = models.CharField(max_length=100, default='', blank=True)
    name = models.CharField(max_length=100, default='', blank=True)
    year = models.CharField(max_length=100, default='', blank=True)
    pdf_f = models.FileField(upload_to="static/pdfs/", default='', blank=True)

    def __str__(self):
        return self.sub

class SemEight(models.Model):
    sub = models.CharField(max_length=100, default='', blank=True)
    name = models.CharField(max_length=100, default='', blank=True)
    year = models.CharField(max_length=100, default='', blank=True)
    pdf_f = models.FileField(upload_to="static/pdfs/", default='', blank=True)

    def __str__(self):
        return self.sub
