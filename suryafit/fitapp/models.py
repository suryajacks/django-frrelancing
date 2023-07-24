from django.db import models


class Student(models.Model):
    Name           = models.CharField(max_length=100)
    Father_name    = models.CharField(max_length=100)
    Age            = models.IntegerField()
    Date_of_birth  = models.DateField()
    address        = models.TextField()
    College        = models.TextField()
    Course         = models.TextField()
    Degree         = models.CharField(max_length =150)
    NEW            = models.BooleanField(blank=True )
    Email          = models.EmailField()
    Mobile_number  =models.IntegerField()
    
def __str__(self):
    return self.Name

class Student1(models.Model):
    Name1           = models.CharField(max_length=100)
    Father_name1    = models.CharField(max_length=100)
    Age1            = models.IntegerField()
    Date_of_birth1  = models.DateField()
    address1        = models.TextField()
    College1        = models.TextField()
    Course1         = models.TextField()
    Degree1         = models.CharField(max_length =150)
    Email1          = models.EmailField()
    Mobile_number1  = models.IntegerField(null=True)
    
def __str__(self):
    return self.Name



class Student_course(models.Model):
    Course1 = models.CharField(max_length=100)
        
class Question2(models.Model):
    Answer1 = models.TextField(50)
    Answer2 = models.TextField(50)
    Answer3 = models.TextField(50)    
   
class Question3(models.Model):
    Answer1 = models.TextField(50)
    Answer2 = models.TextField(50)
    Answer3 = models.TextField(50)   
        
        
        
class Admin_Questions(models.Model):
    Que1 = models.TextField() 
    Que2 = models.TextField() 
    Que3 = models.TextField() 
    Que4 = models.TextField() 
    Que5 = models.TextField() 
    Que6 = models.TextField() 
    Que7 = models.TextField() 
    Que8 = models.TextField() 
    Que9 = models.TextField() 
    Que10 = models.TextField() 
          
        