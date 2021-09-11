from django.contrib import auth
from django.contrib.messages.api import error
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from hostproapp.models import Feedback
from hostproapp.models import Book
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime

def feedback(request):
    if request.method == 'POST':
      # if user !=login:
      #    messages.error(request,"@login_required")
      #    return redirect('home')
   
     
      name = request.POST.get('name')
      lastname = request.POST.get('lastname')
      phone = request.POST.get('phone')
      dfeedback = request.POST.get('dfeedback')
      feedback= Feedback(lastname=lastname, phone=phone,  name=name, dfeedback=dfeedback , date=datetime.today())
      feedback.save()
      messages.success(request, "your feedback submitted")
      # return redirect ('home')
    return render(request, 'feedback.html')




def book(request):
    if request.method == 'POST':
       
     
       
       
      name2 = request.POST.get('name2')
      Lastname = request.POST.get('Lastname')
      Gender = request.POST.get('Gender')
      Age = request.POST.get('Age')
      Disease = request.POST.get('Disease')
      Dname = request.POST.get('Dname')
      date = request.POST.get('date') 
      book = Book(name2=name2, Lastname=Lastname,  Gender=Gender, Age=Age, Disease=Disease, Dname=Dname, date=date  )
      messages.success(request,"booking done sucessfully thankyou")
      book.save()
      
    return render(request, 'book.html')

def base(request):
   return render(request, 'base.html')

def Information(request):
   return render(request, 'Information.html')

def Opt(request):
   return render(request, 'Opt.html')

def Blood(request):
   return render(request, 'Blood.html')

def Emergency(request):
   return render(request, 'Emergency.html')


def handleSignup(request):
      if request.method == 'POST':
             
         username = request.POST['username']
         fname = request.POST['fname']
         lname = request.POST['lname']
         email  = request.POST['email']
         password1 = request.POST['password1']
         password2 = request.POST['password2']

         # chck erroes
         if  password1 != password2:
            messages.error(request, "passwords doesnt match")   
            return redirect( 'home')

         if not username.isalnum():
            messages.error(request, "username is not alphanumeric")   
            return redirect( 'home')
              
          

         myuser = User.objects.create_user(username, email, password1)
         myuser.first_name= fname
         myuser.last_name= lname
         myuser.save()
         messages.success(request, "your  account has been succesful created")

         # value error comes when redirect is npt taken
         return redirect( 'home')


      else:
        return HttpResponse('404 - noty found')       
        
def handleLogin(request):
   if request.method == 'POST':
             
    loginusername = request.POST['loginusername']
    loginpassword = request.POST['loginpassword']

    user = authenticate(username=loginusername, password=loginpassword)

    if user is not None:
       login(request, user )
       messages.success(request, " loged in sucessful")
       return redirect('home')
    else:
      messages.error(request, " loged in unsucessful please tryagain ")   
      return redirect('home') 
           
    
   return HttpResponse('404-not found')


def profile(request):
   return render(request, 'profile.html')
     
def handleLogout(request):
   
   logout(request)
   messages.success(request, " loged out ")
   return redirect('home')
  

def search(request):
   return redirect ('feedback')



def hello(request):
#  if request.method == 'POST':      
  loginusername = request.POST['loginusername']
#   loginpassword = request.POST['loginpassword']
  user = authenticate(username=loginusername, password=loginpassword)
  if user is not None:
     login(request, user )
     messages.success(request, " logged in ")
     return redirect('hello')
  else:
     messages.error(request, " not in ")
     
#  return HttpResponse('404-not found')
   
          
    

@login_required()
def editprofile(request):
  
       if request.method == 'POST':
             
         
         fn = request.POST['fname']
         ln = request.POST['lname']
         em  = request.POST['email']
         un = request.POST['uname']
        

        
              
          

         myuser = User.objects.get(id=request.user.id)
         myuser.first_name= fn
         myuser.last_name= ln
         myuser.username=un
         myuser.email=em
         myuser.save()
   
         messages.success(request, "your  changes done sucessfully!!!")

      

   

        
         return redirect( 'profile')



       else:
        return render(request,'editprofile.html')  


 
def delete(request):
  
       if request.method == 'POST':
             
         
         fn = request.POST['fname']
         ln = request.POST['lname']
         em  = request.POST['email']
         un = request.POST['uname']
        

        
              
          

         myuser = User.objects.get(id=request.user.id)
         myuser.first_name= fn
         myuser.last_name= ln
         myuser.username=un
         myuser.email=em
         myuser.delete()
   
         messages.success(request, "your  account delete permentaley!!!")

      

   

        
         return redirect( '/')



       else:
        return render(request,'delete.html')  