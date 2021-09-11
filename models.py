from django.db import models

# Create your models here.


# Create your models here.
class Feedback(models.Model):
   name = models.CharField(max_length=50,null=True)
   lastname = models.CharField(max_length=50,null=True)
   phone = models.CharField(max_length=50,null=True)
   dfeedback = models.CharField(max_length=50,null=True)
   date = models.DateField(null=True)

   def __str__(self):
            return self.name

class Book(models.Model):
    
   Lastname= models.CharField(max_length=50,null=True)
   name2= models.CharField(max_length=50,null=True)
   Gender= models.CharField(max_length=50,null=True)
   Age= models.CharField(max_length=50)
   Disease= models.CharField(max_length=50)
   Dname= models.CharField(max_length=50,null=True)
   date= models.CharField(max_length=50,null=True)

   def __str__(self):
           return self.name2