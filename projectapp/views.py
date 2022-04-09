from django.shortcuts import render
from django.template import loader
# Create your views here.
from .corelate import get_corelation 
from django.http import HttpResponse
from .forms import InputForm , MyForm
import logging

def index(request):
  return HttpResponse("Hello Geeks")


 
# Create your views here.
def home_view(request):
    context ={}
    context['form']= InputForm()

   

    return render(request,"home.html", context)

from django.views.decorators.csrf import csrf_exempt
import json

from pathlib import Path
@csrf_exempt 
def responseform(request):
 #if form is submitted
     form = MyForm()
     if request.method == 'POST':
        
        myForm = MyForm(request.POST)

        if myForm.is_valid():
            vote=myForm.cleaned_data['radio']
                  
            with open("Test/votes.json","r") as f:
              current = json.load(f)
            current[vote]=current[vote]+1
            with open("Test/votes.json","w") as f:    
              json.dump(current,f)
            context = current
            print('context')
            print(context)
            template = loader.get_template('thankyou.html')
            

            #returing the template
            return HttpResponse(template.render(context,request))



     else:
         form = MyForm()
     #returning form

     return render(request, 'responseform.html', {'form':form});






