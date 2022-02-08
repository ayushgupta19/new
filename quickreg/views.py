from ast import If
import json
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import User, Emailtemplate
from .forms import StudentRegistration, mailregister
from django.http import JsonResponse
from django.core import serializers
from django.core.mail import EmailMessage




def showformdata(request):
    
    
    if request.method  ==  'POST':
        b = json.loads(request.body.decode())
        user = User()
        user.name= b['name']
        user.email= b['email']
        user.phone = b['phone']
        user.typ = b['typ']
        user.col = b['col']
        user.text = b['text']
        user.save()

        return JsonResponse({'kil': 'created'})



def showdata(request):
    
    
    if request.method  ==  'GET':
        wil=User.objects.values()
        
        return JsonResponse({"result":list(wil),"k2":"success"})
        


def showdata1(request, user_id=None):
    
    
    if request.method == 'GET':
        if user_id:
            wil=User.objects.filter(id=user_id).values()
        else:
            wil= list(User.objects.values())
        a =[]
        
        for x in wil:
            b={}
            
            y=x["id"]
            b["user_id"]=y
            for z in x:
                if (z=="id"):
                    continue
                c=x[z]
                z+='_%s' %y
                print("z=",z)
                b[z]=c
            print("x=",b) 
            a.append(b)   
        return JsonResponse({"result":a,"k2":"success"})






def maildata(request):
    
    
    if request.method  ==  'POST':
        fm = mailregister(request.POST)

        if fm.is_valid():
            obj= Emailtemplate()
            obj.to=fm.cleaned_data['to']
            obj.CC=fm.cleaned_data['CC']
            obj.subject=fm.cleaned_data['subject']
            obj.emailbody=fm.cleaned_data['emailbody']
            obj.reply=fm.cleaned_data['reply']
            obj.fields=fm.cleaned_data['fields']
            
            print(obj)
            obj.save()
            fields=fm.cleaned_data['fields']
            fields=json.loads(fields)
            bdy=fm.cleaned_data['emailbody']
            s=fm.cleaned_data['subject']

            f = list(fields.keys())[0]
            user_id = f.split('_')[-1]
            ud = User.objects.get(id=user_id)
            for key, value in fields.items():
                ukey=key.split('_')[0]
                bdy=bdy.replace(value, str(eval('ud.%s'%ukey)))
                s=s.replace(value, str(eval('ud.%s'%ukey)))


            
            eml=EmailMessage(subject=s,body=bdy,from_email='faqritesh@gmail.com',to=[obj.to],cc=[obj.CC])
            eml.send()
            
            return JsonResponse({'kk':True})
    else:
        fm = mailregister()    

    return render(request, 'userregistration.html',{'form': fm})       