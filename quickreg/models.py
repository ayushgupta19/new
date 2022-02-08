from tkinter import Widget
from django.db import models
from django.forms import Textarea

# Create your models here.
sup=(("sreehari@hubbler.mobi","Manager"),("aayushgupta.gupta594@gmail.com", "Assigner"), ("faqritesh@gmail.com", "Creator"))


# Create your models here.
class User(models.Model):
    name= models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    phone = models.BigIntegerField()

    typ = models.TextField(blank=True)
    col =models.CharField(max_length=50, choices= sup, default= 'gashu7320@gmail.com')
    text =models.CharField(max_length=8)


class Emailtemplate(models.Model):
    to =models.CharField(max_length=50, choices= sup, default= 'gashu7320@gmail.com')
    
    CC=models.EmailField(max_length=70)
    reply= models.EmailField(max_length=70)
    subject=models.CharField(max_length=100)
    emailbody=models.TextField(blank=True)
    fields = models.TextField(blank=True)
    
    


    


    