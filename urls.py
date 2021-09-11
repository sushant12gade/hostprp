from django.urls import path
from django.contrib import admin
from.import views

#  django admin header customization
admin.site.site_header = "login to  devloper hostp"
admin.site.site_title = "login to   hostp  dashboard "
admin.site.index_title = "welcome to portal "

urlpatterns = [
path('hello',views.hello, name='hello'),
 path('',views.base, name='home'),
 path('feedback',views.feedback, name='feedback'),
 path('signup',views.handleSignup, name='handleSignup'),
 path('login',views.handleLogin, name='handleLogin'),
 path('logout',views.handleLogout, name='handleLogout'),
 path('book',views.book, name='book'),
 path('Emergency',views.Emergency, name='Emergency'),
 path('Blood',views.Blood, name='Blood'),
 path('Opt',views.Opt, name='Opt'),
 path('Information',views.Information, name=' Information'),
 path('profile',views.profile, name='profile'),
  path('delete',views.delete, name='delete'),
  path('editprofile',views.editprofile, name='editprofile'),
   
]